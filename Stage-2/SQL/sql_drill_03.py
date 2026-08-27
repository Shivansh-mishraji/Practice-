import sqlite3

def setup_db() -> sqlite3.Connection:
    # ✍️ Connect to :memory:, PRAGMA FK ON
    # Create users (id INTEGER PRIMARY KEY, name TEXT)
    # Create resumes (id INTEGER PRIMARY KEY, user_id INTEGER, score INTEGER,
    #                 FOREIGN KEY (user_id) REFERENCES users(id))
    # Insert: users → (1,"Shivansh"), (2,"Priya"), (3,"Rahul")
    # Insert: resumes → (101,1,95), (102,2,88)  [Rahul has NO resume]
    # commit + return conn
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foriegn_key = ON")
    cursor.execute("CREATE TABLE USERS(ID INTEGER PRIMARY KEY, NAME TEXT);")
    cursor.execute("CREATE TABLE RESUME(ID INTEGER PRIMARY KEY, USER_ID INTEGER, SCORE INTEGER, FOREIGN KEY (USER_ID) REFERENCES USERS(ID));")
    cursor.execute("INSERT INTO USERS VALUES (1,'SHIVANSH'), (2,'PRIYA'), (3,'RAHUL');")
    cursor.execute("INSERT INTO RESUME VALUES (101,1,95), (102,2,88);")
    conn.commit()
    return conn

def inner_join(conn: sqlite3.Connection) -> list[tuple]:
    # ✍️ SELECT users.name, resumes.score
    #    FROM users INNER JOIN resumes ON users.id = resumes.user_id
    cursor = conn.cursor()
    cursor.execute("SELECT USERS.NAME, RESUME.SCORE FROM USERS INNER JOIN RESUME ON USERS.ID = RESUME.USER_ID;")
    conn.commit()
    return cursor.fetchall()

def left_join(conn: sqlite3.Connection) -> list[tuple]:
    # ✍️ SELECT users.name, resumes.score
    #    FROM users LEFT JOIN resumes ON users.id = resumes.user_id
    cursor = conn.cursor()
    cursor.execute("SELECT USERS.NAME, RESUME.SCORE FROM USERS LEFT JOIN RESUME ON USERS.ID = RESUME.USER_ID;")
    return cursor.fetchall()

if __name__ == "__main__":
    db = setup_db()

    inner = inner_join(db)
    left  = left_join(db)

    print("INNER JOIN:", inner)
    print("LEFT JOIN: ", left)

    assert len(inner) == 2          # Only Shivansh & Priya
    assert len(left)  == 3          # All 3 users
    assert left[2][1] is None       # Rahul has NULL score

    print("Drill 3 Passed!")
