import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# 1. Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT
)
""")

# 2. Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL
)
""")

# 3. Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")

# Sample Data
cursor.executemany("INSERT OR IGNORE INTO customers VALUES (?, ?, ?)", [
    (1, "Aarav Sharma", "Mumbai"),
    (2, "Priya Patel", "Delhi"),
    (3, "Rohan Mehta", "Bengaluru")
])

cursor.executemany("INSERT OR IGNORE INTO products VALUES (?, ?, ?)", [
    (101, "Mechanical Keyboard", 75.0),
    (102, "Wireless Mouse", 25.0),
    (103, "Ergonomic Chair", 180.0)
])

cursor.executemany("INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 101, 2, "2024-04-01"),
    (2, 2, 103, 1, "2024-04-03"),
    (3, 1, 102, 1, "2024-04-05"),
    (4, 3, 102, 3, "2024-04-10")
])

conn.commit()
conn.close()
print("Database 'company.db' created successfully.")