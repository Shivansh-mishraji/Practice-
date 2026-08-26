"""
Write a function create_database() -> sqlite3.Connection:

Connect to ":memory:"
Create a cursor
Execute SQL DDL: CREATE TABLE users (id INTEGER, name TEXT, role TEXT);
Commit the transaction and return the connection object conn

"""
import sqlite3
def create_database() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, role TEXT);")
    conn.commit()
    return conn


if __name__ == "__main__":
    db = create_database()
    cursor = db.cursor()
    
    # Query sqlite_master to verify the table was actually created
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print("Tables in Database:", tables)
    
    assert ("users",) in tables
    print("Drill 0 Passed!")
