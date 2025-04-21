CREATE TABLE IF NOT EXISTS accounts (
    account_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL DEFAULT 0 CHECK (balance >= 0)
);
