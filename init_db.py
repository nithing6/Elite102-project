import sqlite3

DB_FILE = "bank.db"

# Connect to the database (or create it)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Read and execute the schema file
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

print("Database initialized successfully.")

conn.commit()
conn.close()
