import pandas as pd
from src.db.database import get_connection
from src.config import LOG_EXPORT_FILE
import os

def export_to_csv():
    conn = get_connection()

    df = pd.read_sql_query("SELECT * FROM migration_log", conn)

    os.makedirs(os.path.dirname(LOG_EXPORT_FILE), exist_ok=True)
    df.to_csv(LOG_EXPORT_FILE, index=False)

    conn.close()

    print(f"Exported to {LOG_EXPORT_FILE}")