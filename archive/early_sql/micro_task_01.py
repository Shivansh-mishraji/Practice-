"""
Write 2 functions:

1: insert_user(conn: sqlite3.Connection, user_id: int, name: str, role: str) -> None:
   Runs INSERT INTO users VALUES (?, ?, ?); using parameter substitution.
   Calls conn.commit().
2: get_all_users(conn: sqlite3.Connection) -> list[tuple]:
   Runs SELECT id, name, role FROM users; and returns cursor.fetchall().
"""

import sqlite3

def db_setup() -> sqlite3.Connection:
    conn = sqlite3.Connection(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE USERS(USER_ID INTEGER, NAME TEXT, ROLE TEXT);")
    conn.commit()
    return conn
def insert_user(conn: sqlite3.Connection, USER_ID: int, NAME: str, ROLE: str) -> None:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO USERS VALUES(?, ?, ?);", (USER_ID, NAME, ROLE))
    conn.commit()
def get_all_users(conn: sqlite3.Connection) -> list[tuple]:
    cursor = conn.cursor()
    cursor.execute("SELECT USER_ID, NAME, ROLE FROM USERS;")
    conn.commit()
    return cursor.fetchall()

if __name__ == "__main__":
    db = db_setup()
    
    insert_user(db, 1, "Shivansh", "admin")
    insert_user(db, 2, "Aarav", "user")
    
    users = get_all_users(db)
    print("Users in DB:", users)
    
    assert len(users) == 2
    assert users[0] == (1, "Shivansh", "admin")
    assert users[1] == (2, "Aarav", "user")
    
    print("Micro-task 1 passed!")



