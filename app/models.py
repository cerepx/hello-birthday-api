"""
Database models and initialization logic for the Hello Birthday API.
"""

from app.db import get_connection, ensure_database_exists

# Ensure the database exists before initializing the app
ensure_database_exists()


def init_db() -> None:
    """
    Initialize the MySQL database and create the users table if it doesn't exist.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(255) PRIMARY KEY,
                date_of_birth DATE NOT NULL
            )
        """)
        conn.commit()


def save_user_to_db(username: str, date_of_birth: str) -> None:
    """
    Save or update a user's date of birth in the MySQL database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, date_of_birth)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE date_of_birth = VALUES(date_of_birth)
        """, (username, date_of_birth))
        conn.commit()


def get_user_from_db(username: str):
    """
    Retrieve a user's date of birth from the MySQL database.

    Returns:
        tuple or None: ('YYYY-MM-DD',) or None if user not found.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT date_of_birth FROM users WHERE username = %s", (username,))
        row = cursor.fetchone()
        return (row['date_of_birth'],) if row else None
