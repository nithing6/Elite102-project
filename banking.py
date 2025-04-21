# Import the sqlite3 module to interact with an SQLite database
import sqlite3

# Define the database file name it will store our bank accounts and data
DB_FILE = "bank.db"

# Function to connect to the SQLite database
def connect():
    # This function opens a connection to the database and returns the connection object
    return sqlite3.connect(DB_FILE)

# Function to create a new bank account
def create_account(account_id, name):
    try:
        # Establish a connection to the database
        with connect() as conn:
            # Execute SQL query to insert a new account into the accounts table
            # The ? placeholders will be replaced with account_id and name
            conn.execute("INSERT INTO accounts (account_id, name) VALUES (?, ?)", (account_id, name))
        # If the insert is successful return a success message
        return "Account created successfully."
    except sqlite3.IntegrityError:
        # If an account with the same ID already exists return this message
        return "Account already exists."

# Function to modify an existing account's name
def modify_account(account_id, new_name):
    # Establish a connection to the database
    with connect() as conn:
        # Execute SQL query to update the name of the account with the given account_id
        cur = conn.execute("UPDATE accounts SET name = ? WHERE account_id = ?", (new_name, account_id))
        # If no rows were affected meaning no account found return this message
        if cur.rowcount == 0:
            return "Account not found."
    # If the account was updated return a success message
    return "Account name updated."

# Function to close an existing account
def close_account(account_id):
    # Establish a connection to the database
    with connect() as conn:
        # Execute SQL query to delete the account with the given account_id
        cur = conn.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,))
        # If no rows were affected meaning no account found return this message
        if cur.rowcount == 0:
            return "Account not found."
    # If the account was deleted return a success message
    return "Account closed."

# Function to check the balance of an account
def check_balance(account_id):
    # Establish a connection to the database
    with connect() as conn:
        # Execute SQL query to select the balance of the account with the given account_id
        cur = conn.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        # Fetch the result of the query
        row = cur.fetchone()
        # If an account is found return the balance row 0 contains the balance value
        if row:
            return row[0]
        # If no account is found return this message
        return "Account not found."

# Function to deposit money into an account
def deposit(account_id, amount):
    # Check if the deposit amount is valid it must be greater than 0
    if amount <= 0:
        return "Invalid amount."
    # Establish a connection to the database
    with connect() as conn:
        # Execute SQL query to add the deposit amount to the account's balance
        cur = conn.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_id))
        # If no rows were affected meaning no account found return this message
        if cur.rowcount == 0:
            return "Account not found."
    # If the deposit is successful return a message with the deposit amount
    return f"Deposited ${amount}."

# Function to withdraw money from an account
def withdraw(account_id, amount):
    # Establish a connection to the database
    with connect() as conn:
        # Execute SQL query to fetch the current balance of the account
        cur = conn.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        # Fetch the result of the query
        row = cur.fetchone()
        # If no account is found return this message
        if not row:
            return "Account not found."
        # If the withdrawal amount is greater than the current balance return this message
        if amount > row[0]:
            return "Insufficient funds."
        # Execute SQL query to subtract the withdrawal amount from the account's balance
        conn.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_id))
    # If the withdrawal is successful return a message with the withdrawal amount
    return f"Withdrew ${amount}."
