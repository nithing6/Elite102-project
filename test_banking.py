import unittest
import sqlite3
import os
import banking

DB_FILE = "bank.db"

class TestBanking(unittest.TestCase):

    def setUp(self):
        # Remove old DB if it exists to start fresh
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)

        # Recreate DB using the schema
        with open("schema.sql", "r") as f:
            schema = f.read()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.executescript(schema)
        conn.commit()
        conn.close()

    def test_create_account(self):
        result = banking.create_account("001", "Alice")
        self.assertEqual(result, "Account created successfully.")

    def test_duplicate_account(self):
        banking.create_account("001", "Alice")
        result = banking.create_account("001", "Bob")
        self.assertEqual(result, "Account already exists.")

    def test_deposit_and_withdraw(self):
        banking.create_account("002", "John")
        self.assertEqual(banking.deposit("002", 200), "Deposited $200.")
        self.assertEqual(banking.withdraw("002", 100), "Withdrew $100.")

    def test_insufficient_funds(self):
        banking.create_account("003", "Sarah")
        result = banking.withdraw("003", 50)
        self.assertEqual(result, "Insufficient funds.")

    def test_check_balance(self):
        banking.create_account("004", "Eve")
        banking.deposit("004", 500)
        balance = banking.check_balance("004")
        self.assertEqual(balance, 500)

    def test_modify_account(self):
        banking.create_account("005", "Bob")
        result = banking.modify_account("005", "Robert")
        self.assertEqual(result, "Account name updated.")

    def test_close_account(self):
        banking.create_account("006", "Chad")
        result = banking.close_account("006")
        self.assertEqual(result, "Account closed.")

if __name__ == "__main__":
    unittest.main()
