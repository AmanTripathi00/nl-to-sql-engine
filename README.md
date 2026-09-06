# Semantic Text-to-SQL Engine with NLG Explanation

An end-to-end AI application that converts natural language queries into syntactically validated SQL, executes them against a relational SQLite database, and generates executive summaries using Natural Language Generation (NLG).

🔗 **Live Demo:** [Streamlit Cloud App](https://nl-to-sql-engine-fzrxuyujckj2b6scwdch5s.streamlit.app)

---

## 📌 Features
- **Natural Language to SQL:** Generates schema-aware SQL from user prompts via Groq Cloud API.
- **Syntax Validation:** Validates generated SQL using `sqlglot` prior to execution.
- **Relational Execution:** Runs queries directly against an integrated SQLite database (`sales.db`).
- **NLG Summaries:** Translates tabular query output into clear business insights.
- **Interactive UI:** Built with Streamlit for quick, responsive experimentation.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Frontend / Framework:** Streamlit
- **Database:** SQLite
- **LLM Provider:** Groq Cloud API
- **SQL Parser & Validator:** `sqlglot`
- **Data Manipulation:** `pandas`

---

## 🗄️ Database Schema
The database models an e-commerce catalog and order management system:
- **`customers`** (`customer_id`, `name`, `city`)
- **`products`** (`product_id`, `product_name`, `price`)
- **`orders`** (`order_id`, `customer_id`, `product_id`, `quantity`, `order_date`)

---

## 💡 Example Queries
- *Which product has the highest price?*
- *Show total spending for each customer.*
- *List all customers who live in Mumbai.*
- *Which customer bought the Ergonomic Chair?*
- 
