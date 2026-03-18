import sqlite3
from src.config import DB_FILE

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS migration_log (
        manatal_id INTEGER PRIMARY KEY,
        ashby_id TEXT,
        cv BOOLEAN,
        notes BOOLEAN,
        tags BOOLEAN,
        error TEXT
    )
    """)

    conn.commit()
    conn.close()