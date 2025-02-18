import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None = None
curs: Cursor | None = None

def get_db(name: str | None = None, reset: bool = False):
    """Connect to SQLite database file"""
    global conn, curs
    if conn:
        if not reset:
            return
        conn = None
    if not name:
        name = os.getenv("RECTANGLE_SQLITE_DB")
        top_dir = Path(__file__).resolve().parents[1]  # repo top    
        db_dir = top_dir / "db"
        db_name = "rectangle.db"
        db_path = str(db_dir / db_name)
        name = os.getenv("RECTANGLE_SQLITE_DB", db_path)

    if not db_dir.exists():
        db_dir.mkdir(parents=True, exist_ok=True)  # Ensure db directory exists

    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()
    
    # Create tables if they don’t exist
    curs.execute("""CREATE TABLE IF NOT EXISTS rectangle(
                 width FLOAT, 
                 height FLOAT,
                 PRIMARY KEY (width, height))""")
    
    conn.commit()  # Ensure the table is created before preloading data

    # preload_data()  # Call function to preload data

def preload_data():
    """Preload database only if no rectangles exist"""
    from model.rectangle import Rectangle
    from data.rectangle import create

    curs.execute("SELECT COUNT(*) FROM rectangle")
    count = curs.fetchone()[0]

    if count > 0:
        print("✅ Database already has data. Skipping preload.")
        return

    _rectangles = [
        Rectangle(width=10, height=5),
        Rectangle(width=20, height=25),
        Rectangle(width=1, height=1),
        Rectangle(width=8, height=15),
        Rectangle(width=4.7, height=1.1),
        Rectangle(width=3, height=1.4)
    ]

    for rect in _rectangles:
        try:
            create(rect)
        except IntegrityError:
            pass  # Ignore duplicates

    conn.commit()
    print("✅ Database preloaded with rectangles!")


get_db()  # Ensure DB is initialized
