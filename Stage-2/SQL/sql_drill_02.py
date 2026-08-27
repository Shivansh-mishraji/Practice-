"""
Implement setup_relational_db() -> sqlite3.Connection:

Connect to ":memory:"
Create cursor
PRAGMA foreign_keys = ON
Create users table: id INTEGER PRIMARY KEY, name TEXT NOT NULL
Create resumes table: id INTEGER PRIMARY KEY, user_id INTEGER, score INTEGER + FOREIGN KEY (user_id) REFERENCES users(id)
Insert user (1, "Shivansh")
Insert resume (101, 1, 95)
conn.commit() → return conn
"""
import sqlite3

def setup_relational_db() -> sqlite3.Connection:
    # ✍️ Write from memory
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL);")
    cursor.execute("CREATE TABLE resumes(id INTEGER PRIMARY KEY, user_id INTEGER, score INTEGER, FOREIGN KEY (user_id) REFERENCES users(id));")
    cursor.execute("INSERT INTO users VALUES(1, 'Shivansh');")
    cursor.execute("INSERT INTO resumes VALUES(101, 1, 95);")
    conn.commit()
    return conn
        

if __name__ == "__main__":
    db = setup_relational_db()
    cursor = db.cursor()

    users = cursor.execute("SELECT * FROM users;").fetchall()
    resumes = cursor.execute("SELECT * FROM resumes;").fetchall()

    print("Users:", users)
    print("Resumes:", resumes)

    assert len(users) == 1
    assert len(resumes) == 1
    assert resumes[0][1] == 1  # user_id must be 1

    try:
        cursor.execute("INSERT INTO resumes VALUES (102, 999, 80);")
        print("FAILED: Orphan record was allowed!")
        assert False
    except sqlite3.IntegrityError:
        print("PASSED: FK constraint blocked orphan record!")

    print("Drill 2 Passed!")


