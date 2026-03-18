import sys
from src.db.database import init_db
from src.services.migration import migrate
from src.utils.exporter import export_to_csv

def main():
    init_db()

    if len(sys.argv) > 1 and sys.argv[1] == "export":
        export_to_csv()
    else:
        migrate()

if __name__ == "__main__":
    main()