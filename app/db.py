import os
import sqlite3
from contextlib import contextmanager

DATABASE_PATH = "birthday.db"

@contextmanager
def get_connection():
    """
    Context manager to get a SQLite3 database connection.

    Yields:
        sqlite3.Connection: SQLite3 connection object.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Enable dictionary-like row access
    try:
        yield conn
    finally:
        conn.close()