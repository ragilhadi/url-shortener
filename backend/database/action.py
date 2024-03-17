import sqlite3
from typing import Tuple


class URLAction:
    def initalize_schema(self):
        """
        Initialize schema.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS url (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                url_short TEXT NOT NULL UNIQUE,
                valid_until DATETIME NOT NULL
            )''')
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    def get_url_by_id(self, id_url: int) -> Tuple[bool, list]:
        """
        Get URL by ID.

        Args:
            id_url (int): URL ID.
        
        Returns:
            Tuple[bool, list]: A tuple containing the status and URL data.
        """
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM url WHERE id = {id_url}")
            url = cursor.fetchone()
            conn.close()
            return True, url
        except Exception as e:
            print(e)
            return False, []

    def get_count_url(self) -> Tuple[bool, int]:
        """
        Get count of URLs.

        Returns:
            int: Count of URLs.
        """
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM url")
            count = cursor.fetchone()
            cursor.close()
            conn.close()
            return True, count[0]
        except Exception as e:
            print(e)
            return False, 0

    def add_url(self, url, url_short, valid_until):
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            if (valid_until == ""):
                valid_until = "2045-12-31 23:59:59"
            cursor.execute(
                """INSERT INTO url (url, url_short, valid_until)
                      VALUES (?, ?, ?)""",
                (url, url_short, valid_until),
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()
