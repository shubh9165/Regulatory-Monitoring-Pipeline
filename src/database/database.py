import sqlite3

DB_NAME = "monitoring.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monitoring (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT UNIQUE,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()


def get_old_data(website):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT data FROM monitoring WHERE website = ?",
        (website,)
    )

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else ""


def update_old_data(website, data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO monitoring (website, data)
        VALUES (?, ?)
        ON CONFLICT(website)
        DO UPDATE SET data = excluded.data
    """, (website, data))

    conn.commit()
    conn.close()