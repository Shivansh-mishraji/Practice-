import sqlite3

def setup_accounts_db() -> sqlite3.Connection:
    # Create accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL)
    # Insert: (1, "Shivansh", 1000.0), (2, "Priya", 500.0)
    # commit + return conn
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE accounts(id INTEGER PRIMARY KEY, name TEXT, balance REAL);")
    cursor.execute("INSERT INTO accounts VALUES (1, 'Shivansh',1000.0), (2, 'Priya', 500.0);")
    conn.commit()
    return conn

def transfer_money(conn: sqlite3.Connection, from_id: int, to_id: int, amount: float) -> None:
    # ✍️ Wrap in try/except:
    # - Deduct from sender using ATOMIC SQL (WHERE balance >= amount)
    # - Check cursor.rowcount == 0 → rollback + raise ValueError("Insufficient funds")
    # - Credit receiver
    # - conn.commit()
    # - On ANY exception → conn.rollback() + re-raise
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE accounts.id = ? AND balance >= ?;",(amount,from_id,amount))
        if cursor.rowcount == 0:
                conn.rollback()
                raise ValueError("Insufficient funds")
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE accounts.id = ?;",(amount,to_id))
        conn.commit()
    except Exception as e:
         conn.rollback()
         raise e
        
if __name__ == "__main__":
    db = setup_accounts_db()

    # Test 1: Valid transfer ₹200 from Shivansh to Priya
    transfer_money(db, 1, 2, 200.0)
    balances = db.cursor().execute("SELECT name, balance FROM accounts;").fetchall()
    print("After valid transfer:", balances)
    assert balances[0][1] == 800.0   # Shivansh: 1000-200
    assert balances[1][1] == 700.0   # Priya: 500+200

    # Test 2: Invalid transfer — Priya tries to send ₹1000 (she only has ₹700)
    try:
        transfer_money(db, 2, 1, 1000.0)
        print("FAILED: Allowed overdraft!")
        assert False
    except ValueError as e:
        print(f"PASSED: Correctly blocked — {e}")

    # Verify balances unchanged after failed transfer
    balances = db.cursor().execute("SELECT name, balance FROM accounts;").fetchall()
    print("After failed transfer:", balances)
    assert balances[0][1] == 800.0   # Shivansh unchanged
    assert balances[1][1] == 700.0   # Priya unchanged

    print("Drill 4 Passed!")
