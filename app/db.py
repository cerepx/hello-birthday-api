"""
Database connection utilities for the Hello Birthday API.
Handles MySQL connection retries on startup and ensures the database exists.
"""

from typing import Optional
import os
import time
import pymysql


# Environment configuration
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


def _connect_to_mysql(database: Optional[str] = None) -> pymysql.connections.Connection:
    """
    Establish a connection to the MySQL server.

    Args:
        database (Optional[str]): Database name to connect to.

    Returns:
        pymysql.connections.Connection: Active MySQL connection.
    """
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=database,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


def get_connection(retries: int = 10, delay: int = 2) -> pymysql.connections.Connection:
    """
    Attempt to connect to MySQL with retries.

    Args:
        retries (int): Number of retry attempts.
        delay (int): Delay between retries in seconds.

    Returns:
        pymysql.connections.Connection: Active MySQL connection with selected database.
    """
    for attempt in range(1, retries + 1):
        try:
            return _connect_to_mysql(database=MYSQL_DATABASE)
        except pymysql.err.OperationalError as db_error:
            print(f"[DB Retry] Attempt {attempt}/{retries}: {db_error}")
            time.sleep(delay)

    raise ConnectionError(
        f"Could not connect to MySQL database `{MYSQL_DATABASE}` "
        f"after {retries} retries."
    )


def ensure_database_exists(retries: int = 10, delay: int = 2) -> None:
    """
    Ensure the specified MySQL database exists; create it if missing.

    Args:
        retries (int): Number of retry attempts.
        delay (int): Delay between retries in seconds.

    Raises:
        ConnectionError: If database creation fails after all retries.
    """
    for attempt in range(1, retries + 1):
        try:
            connection = _connect_to_mysql()
            with connection.cursor() as cursor:
                cursor.execute(
                    f"CREATE DATABASE IF NOT EXISTS `{MYSQL_DATABASE}`")
            connection.commit()
            print(
                f"[DB] Database `{MYSQL_DATABASE}` created or already exists.")
            connection.close()
            return
        except pymysql.err.OperationalError as db_error:
            print(
                f"[DB Retry] (ensure_database_exists) Attempt {attempt}/{retries}: {db_error}")
            time.sleep(delay)

    raise ConnectionError(
        f"Could not ensure database `{MYSQL_DATABASE}` exists "
        f"after {retries} retries."
    )
