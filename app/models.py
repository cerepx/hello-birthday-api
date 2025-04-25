from app.db import get_connection

def init_db() -> None:
    """
    Initialize the SQLite database and create the users table if it doesn't exist.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                date_of_birth TEXT NOT NULL
            )
        """)
        conn.commit()

def save_user_to_db(username: str, date_of_birth: str) -> None:
    """
    Save or update a user's date of birth in the SQLite database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, date_of_birth)
            VALUES (?, ?)
            ON CONFLICT(username) DO UPDATE SET date_of_birth = excluded.date_of_birth
        """, (username, date_of_birth))
        conn.commit()

def get_user_from_db(username: str):
    """
    Retrieve a user's date of birth from the SQLite database.

    Returns:
        tuple or None: ('YYYY-MM-DD',) or None if user not found.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT date_of_birth FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return (row["date_of_birth"],) if row else None