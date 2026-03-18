from src.db.database import get_connection

def log_candidate(manatal_id, ashby_id, cv, notes, tags, error=""):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO migration_log
        (manatal_id, ashby_id, cv, notes, tags, error)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (manatal_id, ashby_id, cv, notes, tags, error))

    conn.commit()
    conn.close()


def get_last_processed_id():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(manatal_id) FROM migration_log")
    result = cursor.fetchone()[0]

    conn.close()
    return result