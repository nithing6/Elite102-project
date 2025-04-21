# Import the unittest module for writing tests
import unittest
# Import the sqlite3 module for interacting with the database
import sqlite3
# Import the os module for file operations
import os
# Import the banking module to test its functions
import banking

# Define the database file name
DB_FILE = "bank.db"

# Create a class to test the banking functions
class TestBanking(unittest.TestCase):

    # Set up the testing environment
    def setUp(self):
        # Remove old DB if it exists to start fresh
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)

        # Recreate DB using the schema
        with open("schema.sql", "r") as f:
            schema = f.read()

        # Establish a connection to the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Execute the schema to set up the accounts table
        cursor.executescript(schema)
        # Commit changes and close the connection
        conn.commit()
        conn.close()

    # Test creating an account successfully
    def test_create_account(self):
        # Call the create_account function and check if the result is correct
        result = banking.create_account("001", "Alice")
        self.assertEqual(result, "Account created successfully.")

    # Test creating a duplicate account
    def test_duplicate_account(self):
        # Create an account then try to create another account with the same ID
        banking.create_account("001", "Alice")
        result = banking.create_account("001", "Bob")
        self.assertEqual(result, "Account already exists.")

    # Test depositing and withdrawing money from an account
    def test_deposit_and_withdraw(self):
        # Create an account and test depositing and withdrawing money
        banking.create_account("002", "John")
        self.assertEqual(banking.deposit("002", 200), "Deposited $200.")
        self.assertEqual(banking.withdraw("002", 100), "Withdrew $100.")

    # Test withdrawing money when there are insufficient funds
    def test_insufficient_funds(self):
        # Create an account and try withdrawing more money than available
        banking.create_account("003", "Sarah")
        result = banking.withdraw("003", 50)
        self.assertEqual(result, "Insufficient funds.")

    # Test checking the balance of an account
    def test_check_balance(self):
        # Create an account deposit some money and check the balance
        banking.create_account("004", "Eve")
        banking.deposit("004", 500)
        balance = banking.check_balance("004")
        self.assertEqual(balance, 500)

    # Test modifying an account's name
    def test_modify_account(self):
        # Create an account and test changing its name
        banking.create_account("005", "Bob")
        result = banking.modify_account("005", "Robert")
        self.assertEqual(result, "Account name updated.")

    # Test closing an account
    def test_close_account(self):
        # Create an account and test closing it
        banking.create_account("006", "Chad")
        result = banking.close_account("006")
        self.assertEqual(result, "Account closed.")

# Run the tests if this file is run as a script
if __name__ == "__main__":
    unittest.main()
