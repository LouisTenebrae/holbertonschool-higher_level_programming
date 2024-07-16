import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('products.db')
c = conn.cursor()

# Create the products table
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Insert some sample data
c.executemany('''
INSERT INTO products (id, name, category, price)
VALUES (?, ?, ?, ?)
''', [
    (1, 'Laptop', 'Electronics', 799.99),
    (2, 'Coffee Mug', 'Home Goods', 15.99)
])

# Commit the changes and close the connection
conn.commit()
conn.close()
