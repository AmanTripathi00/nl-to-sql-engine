import sqlite3
import pandas as pd
import streamlit as st
from groq import Groq
import sqlglot

st.set_page_config(page_title="NL-to-SQL Generator", layout="wide")
st.title("Semantic Text-to-SQL Engine with NLG Explanation")

api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

DATABASE_SCHEMA = """
Tables:
1. customers(customer_id INTEGER, name TEXT, city TEXT)
2. products(product_id INTEGER, product_name TEXT, price REAL)
3. orders(order_id INTEGER, customer_id INTEGER, product_id INTEGER, quantity INTEGER, order_date TEXT)
"""

def generate_sql(client, question):
    system_prompt = f"""
    You are an expert SQL translator. Convert natural language questions into valid SQLite queries based on this schema:
    {DATABASE_SCHEMA}

    Rules:
    - Output ONLY the raw SQL query. Do NOT use markdown formatting or ```sql.
    - Do not write any explanations.
    """
    response = client.chat.completions.create(
       model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content.strip().replace("```sql", "").replace("```", "")

def explain_results(client, question, sql_query, result_df):
    system_prompt = "You are a data analyst. Write a concise 2-sentence executive summary explaining the findings based on the user's question, SQL query, and dataframe result."
    content = f"Question: {question}\nSQL: {sql_query}\nData:\n{result_df.to_string()}"
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

user_question = st.text_input("Ask a question about sales, products, or customers:", "Show total spending for each customer")

if st.button("Generate & Run Query"):
    if not api_key:
        st.error("Please enter your Groq API Key in the left sidebar.")
    else:
        client = Groq(api_key=api_key)
        
        with st.spinner("Generating SQL query..."):
            raw_sql = generate_sql(client, user_question)
            
        st.subheader("1. Generated SQL Query")
        st.code(raw_sql, language="sql")
        
        try:
            sqlglot.transpile(raw_sql, read="sqlite")
            st.success("SQL syntax validated successfully.")
            
            conn = sqlite3.connect("company.db")
            df = pd.read_sql_query(raw_sql, conn)
            conn.close()
            
            st.subheader("2. Query Execution Result")
            st.dataframe(df)
            
            with st.spinner("Generating natural language summary..."):
                summary = explain_results(client, user_question, raw_sql, df)
            
            st.subheader("3. NLG Executive Summary")
            st.info(summary)
            
        except Exception as e:
            st.error(f"Execution Error: {e}")