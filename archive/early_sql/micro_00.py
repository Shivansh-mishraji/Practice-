import sqlite3

def create_db() -> sqlite3.Connection:
    # Write 4 lines here
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE USERS(ID INTEGER, NAME TEXT, ROLE TEXT);")
    conn.commit()
    return conn
    

if __name__ == "__main__":
    db = create_db()
    tables = db.cursor().execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print("Tables:", tables)
    assert ("USERS",) in tables
    print("Micro-task 0 passed!")
