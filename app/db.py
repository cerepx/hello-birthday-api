"""
Database connection utilities for the Hello Birthday API.
Handles MySQL connection retries on startup.
"""

import os
import time
import pymysql


def get_connection(retries=10, delay=2):
    """
    Attempt to connect to MySQL, retrying on failure.

    Args:
        retries (int): Number of retry attempts.
        delay (int): Seconds to wait between attempts.

    Raises:
        Exception: If connection fails after all retries.
    """
    for attempt in range(1, retries + 1):
        try:
            return pymysql.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DB"),
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as db_error:
            print(f"[DB Retry] Attempt {attempt}/{retries}: {db_error}")

            time.sleep(delay)

    raise ConnectionError("Could not connect to MySQL after multiple retries.")
