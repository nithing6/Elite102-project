import sqlite3

DB_FILE = "bank.db"

def connect():
    return sqlite3.connect(DB_FILE)

def create_account(account_id, name):
    try:
        with connect() as conn:
            conn.execute("INSERT INTO accounts (account_id, name) VALUES (?, ?)", (account_id, name))
        return "Account created successfully."
    except sqlite3.IntegrityError:
        return "Account already exists."

def modify_account(account_id, new_name):
    with connect() as conn:
        cur = conn.execute("UPDATE accounts SET name = ? WHERE account_id = ?", (new_name, account_id))
        if cur.rowcount == 0:
            return "Account not found."
    return "Account name updated."

def close_account(account_id):
    with connect() as conn:
        cur = conn.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,))
        if cur.rowcount == 0:
            return "Account not found."
    return "Account closed."

def check_balance(account_id):
    with connect() as conn:
        cur = conn.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        row = cur.fetchone()
        if row:
            return row[0]
        return "Account not found."

def deposit(account_id, amount):
    if amount <= 0:
        return "Invalid amount."
    with connect() as conn:
        cur = conn.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_id))
        if cur.rowcount == 0:
            return "Account not found."
    return f"Deposited ${amount}."

def withdraw(account_id, amount):
    with connect() as conn:
        cur = conn.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        row = cur.fetchone()
        if not row:
            return "Account not found."
        if amount > row[0]:
            return "Insufficient funds."
        conn.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_id))
    return f"Withdrew ${amount}."
