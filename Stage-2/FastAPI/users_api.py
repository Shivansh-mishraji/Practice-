import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Users API", version="1.0.0")

# ─── DB Setup (module-level, runs once at startup) ───────────────────────────
def get_db() -> sqlite3.Connection:
    """Create in-memory DB with users table pre-seeded"""
    # ✍️ Connect to :memory:
    # ✍️ PRAGMA foreign_keys = ON
    # ✍️ CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)
    # ✍️ INSERT 3 users: (1,"Shivansh","s@dev.com"), (2,"Priya","p@dev.com"), (3,"Rahul","r@dev.com")
    # ✍️ commit + return conn
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL);")
    cursor.execute("INSERT INTO users VALUES (1,'Shivansh','s@dev.com'), (2,'Priya','p@dev.com'), (3,'Rahul','r@dev.com');")
    conn.commit()
    return conn

DB = get_db()  # Single shared connection

# ─── Pydantic Schema ─────────────────────────────────────────────────────────
class UserCreate(BaseModel):
    name: str
    email: str

# ─── Routes ──────────────────────────────────────────────────────────────────
@app.get("/users")
def list_users() -> list[dict]:
    """Return all users from DB"""
    # ✍️ SELECT id, name, email FROM users
    # ✍️ return list of dicts: [{"id": 1, "name": "Shivansh", "email": "s@dev.com"}, ...]
    cursor = DB.cursor()
    cursor.execute("SELECT id, name, email FROM users;")
    rows = cursor.fetchall()
    return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]

@app.get("/users/{user_id}")
def get_user( user_id: int) -> dict:
    """Return single user by ID, raise 404 if not found"""
    # ✍️ from fastapi import HTTPException
    # ✍️ SELECT id, name, email FROM users WHERE id = ?
    # ✍️ if no row → raise HTTPException(status_code=404, detail="User not found")
    # ✍️ return the user dict
    cursor = DB.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?;",(user_id,))

    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": row[0], "name": row[1], "email": row[2]}

    
@app.post("/users", status_code=201)
def create_user( user: UserCreate) -> dict:
    """Insert new user into DB, return created user with id"""
    # ✍️ INSERT INTO users (name, email) VALUES (?, ?)
    # ✍️ commit
    # ✍️ return {"id": cursor.lastrowid, "name": user.name, "email": user.email}
    cursor = DB.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?);",(user.name,user.email))
    DB.commit()
    return {"id": cursor.lastrowid, "name": user.name, "email": user.email}