import sqlite3

# ─────────────────────────────────────────────
# PART 1: Setup — DDL + FK + Index
# ─────────────────────────────────────────────
def setup_db() -> sqlite3.Connection:
    """
    - Connect to :memory:
    - PRAGMA foreign_keys = ON
    - CREATE TABLE users    (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)
    - CREATE TABLE orders   (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL,
                             FOREIGN KEY (user_id) REFERENCES users(id))
    - CREATE INDEX idx_orders_user_id ON orders(user_id)
    - INSERT users: (1,"Shivansh","s@dev.com"), (2,"Priya","p@dev.com"), (3,"Rahul","r@dev.com")
    - INSERT orders: (101,1,500.0), (102,1,200.0), (103,2,350.0)  [Rahul has NO orders]
    - commit + return conn
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL);")
    cursor.execute("CREATE TABLE orders   (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL,FOREIGN KEY (user_id) REFERENCES users(id));")
    cursor.execute("CREATE INDEX idx_orders_user_id ON orders(user_id);")
    cursor.execute("INSERT INTO users VALUES(1,'Shivansh','s@dev.com'), (2,'Priya','p@dev.com'), (3,'Rahul','r@dev.com');")
    cursor.execute("INSERT INTO orders VALUES(101,1,500.0), (102,1,200.0), (103,2,350.0);")
    conn.commit()
    return conn

# ─────────────────────────────────────────────
# PART 2: JOINs
# ─────────────────────────────────────────────
def get_users_with_orders(conn: sqlite3.Connection) -> list[tuple]:
    """INNER JOIN — return only users who have at least 1 order"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users INNER JOIN orders ON orders.user_id = users.id;")
    return cursor.fetchall()

def get_all_users_with_orders(conn: sqlite3.Connection) -> list[tuple]:
    """LEFT JOIN — return ALL users, NULL for users with no orders"""
    cursor = conn.cursor()
    cursor.execute("SELECT users.name, users.email, orders.amount FROM users LEFT JOIN orders ON orders.user_id = users.id;")
    return cursor.fetchall()
    

# ─────────────────────────────────────────────
# PART 3: Atomic Transaction
# ─────────────────────────────────────────────
def place_order(conn: sqlite3.Connection, user_id: int, amount: float) -> None:
    """
    Safely insert a new order inside a transaction.
    - try: INSERT INTO orders VALUES (NULL, user_id, amount)
    - conn.commit()
    - except: conn.rollback() + re-raise
    """
    cursor = conn.cursor()
    try:
        
        if amount <= 0 :
            raise ValueError("amount cannot be less than or equal to 0")
        cursor.execute("INSERT INTO orders VALUES(NULL, ?, ?);",(user_id, amount))
        
    except Exception as e:
        conn.rollback()
        raise e
    else:
        conn.commit()

def get_query_plan(conn: sqlite3.Connection, query: str) -> str:
    """Run EXPLAIN QUERY PLAN on given query, return the detail string"""
    cursor = conn.cursor()
    cursor.execute(f"EXPLAIN QUERY PLAN {query} ")
    return cursor.fetchone()[-1]


# ─────────────────────────────────────────────
# TEST HARNESS — Do NOT modify below this line
# ─────────────────────────────────────────────
if __name__ == "__main__":
    db = setup_db()
    c  = db.cursor()

    # Test 1: FK — orphan insert must fail
    try:
        c.execute("INSERT INTO orders VALUES (999, 999, 1.0);")
        print("FAILED: Orphan order allowed!"); assert False
    except sqlite3.IntegrityError:
        print("✅ Test 1 Passed: FK blocked orphan order")

    # Test 2: INNER JOIN — only Shivansh & Priya
    inner = get_users_with_orders(db)
    assert len(inner) == 3, f"Expected 3 rows (Shivansh x2, Priya x1), got {len(inner)}"
    print("✅ Test 2 Passed: INNER JOIN →", inner)

    # Test 3: LEFT JOIN — all 3 users, Rahul has NULL
    left = get_all_users_with_orders(db)
    assert len(left) == 4, f"Expected 4 rows, got {len(left)}"  # Shivansh x2, Priya x1, Rahul(NULL) x1
    assert any(row[2] is None for row in left), "Rahul should have NULL amount"
    print("✅ Test 3 Passed: LEFT JOIN →", left)

    # Test 4: Transaction — place new order
    place_order(db, 2, 800.0)
    orders = c.execute("SELECT * FROM orders WHERE user_id = 2;").fetchall()
    assert len(orders) == 2
    print("✅ Test 4 Passed: New order placed →", orders)

    # Test 5: Index query plan
    plan = get_query_plan(db, "SELECT * FROM orders WHERE user_id = 1;")
    assert "SEARCH" in plan and "idx_orders_user_id" in plan, f"Index not used! Plan: {plan}"
    print("✅ Test 5 Passed: Index used →", plan)

    print("\n🏆 SQL FINAL ASSESSMENT PASSED — 5/5 Tests!")
