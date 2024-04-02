import sqlite3


def initialize_schema():
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
