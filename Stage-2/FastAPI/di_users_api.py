"""
Implement this from scratch in a blank file:

get_db() Generator Dependency:
Connect to :memory: with check_same_thread=False
Set conn.row_factory = sqlite3.Row (allows dict(row) or accessing columns by name like row["name"]!)
Execute table creation & seed 3 users (Shivansh, Priya, Rahul)
yield conn
finally: conn.close()
Pydantic Schemas:
UserCreate(name: str, email: str)
UserResponse(id: int, name: str, email: str)
Endpoints (All using db: sqlite3.Connection = Depends(get_db)):
GET /users ➔ returns list[UserResponse]
GET /users/{user_id} ➔ returns UserResponse (raises HTTPException(404) if not found)
POST /users (status 201) ➔ inserts new user and returns UserResponse
"""

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect(":memory:", check_same_thread = False)
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT);")
    cursor.execute("INSERT INTO users (name, email) VALUES('Shivansh', 'shivay@gmail.com'), ('Priya', 'priya@123'), ('Rahul', 'rahul@123');")
    conn.commit()
    try :
        yield conn
    finally:
        conn.close()

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponce(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users")
def get_all_users(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM users;")
    rows = cursor.fetchall()
    return [dict(r) for r in rows]

@app.get("/users/{user_id}", response_model = UserResponce)
def get_user(user_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?;", (user_id,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not Found")
    return dict(user)

@app.post("/users", status_code = 201)
def create_user(user: UserCreate, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES(?, ?);", (user.name, user.email))
    db.commit()
    id = cursor.lastrowid
    return ({"id": id, "name": user.name, "email": user.email} )

    