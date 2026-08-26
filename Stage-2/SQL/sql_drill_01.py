"""
Use ? placeholders for parameter binding:
 cursor.execute("INSERT INTO users VALUES (?, ?, ?);", (user_id, name, role))
Commit on the connection: conn.commit()
Retrieve all rows: cursor.execute("SELECT id, name, role FROM users;") 
and return cursor.fetchall()
"""
import sqlite3
def setup_database() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users( user_id INTEGER, name TEXT, role TEXT);")
    conn.commit()
    return conn
def insert_user(conn: sqlite3.Connection, user_id: int, name: str, role: str) -> None:
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?,?);",(user_id, name, role))
    conn.commit()
def get_all_users(conn: sqlite3.Connection) ->list[tuple]:
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, role FROM users;")
    return cursor.fetchall()



if __name__ == "__main__":
    db = setup_database()
    
    insert_user(db, 1, "Shivansh", "admin")
    insert_user(db, 2, "Priya", "developer")
    
    users = get_all_users(db)
    print("Users in Database:", users)
    
    assert len(users) == 2
    assert users[0] == (1, "Shivansh", "admin")
    assert users[1] == (2, "Priya", "developer")
    
    print("Drill 1 Passed!")