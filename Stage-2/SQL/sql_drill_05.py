import sqlite3

def setup_indexed_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # 1. Create table users (id INTEGER PRIMARY KEY, email TEXT NOT NULL, name TEXT)
    # 2. Insert dummy user (1, "shivansh@example.com", "Shivansh")
    # 3. Create an index on the 'email' column: CREATE INDEX idx_users_email ON users(email);
    # 4. commit + return conn
    
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT NOT NULL, name TEXT);")
    cursor.execute("INSERT INTO users VALUES(1, 'shivansh@example.com', 'Shivansh');")
    cursor.execute("CREATE INDEX idx_users_email ON users(email);")
    conn.commit()
    return conn

def get_query_plan(conn: sqlite3.Connection, query: str) -> str:
    # ✍️ Run "EXPLAIN QUERY PLAN " + query and return the plan explanation string
    cursor = conn.cursor()
    cursor.execute(f"EXPLAIN QUERY PLAN {query}")
    # SQLite returns rows like (id, parent, notused, detail_text)
    # Return the detail text (last column)
    return cursor.fetchone()[-1]

if __name__ == "__main__":
    db = setup_indexed_db()

    # Query 1: Searching by 'name' (NO index exists on name)
    plan_name = get_query_plan(db, "SELECT * FROM users WHERE name = 'Shivansh';")
    print("Plan for 'name' search (Unindexed):", plan_name)
    assert "SCAN" in plan_name   # Proves full table scan O(N)

    # Query 2: Searching by 'email' (Index idx_users_email EXISTS)
    plan_email = get_query_plan(db, "SELECT * FROM users WHERE email = 'shivansh@example.com';")
    print("Plan for 'email' search (Indexed):  ", plan_email)
    assert "SEARCH" in plan_email and "USING INDEX idx_users_email" in plan_email  # Proves B-Tree index O(log N)

    print("Drill 5 Passed!")
