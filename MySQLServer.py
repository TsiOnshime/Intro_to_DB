import os
import mysql.connector
from mysql.connector import Error

def main():
    host = os.environ.get("MYSQL_HOST", "localhost")
    user = os.environ.get("MYSQL_USER", "root")
    password = os.environ.get("MYSQL_PASSWORD", "")

    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if conn is not None and conn.is_connected():
            try:
                conn.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
