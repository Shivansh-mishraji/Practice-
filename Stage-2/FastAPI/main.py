"""
Import FastAPI from fastapi
Create app = FastAPI(title="Resume API", version="1.0.0")
Implement these 3 routes from scratch:
GET  /              → returns {"status": "ok", "message": "Resume API is running"}
GET  /health        → returns {"healthy": True}
GET  /users/{user_id} → returns {"user_id": user_id, "name": "Shivansh"}
The {user_id} in the last route is a path parameter — it's an int.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Resume API", version="1.0.0")

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.get("/")
def home_screen():
    return {"status": "ok", "message": "Resume API is running"}

@app.get("/health")
def health():
    return {"healthy": True}

@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict:
    return {"user_id": user_id, "name": "Shivansh"}

@app.post("/users")
def create_user(user: UserCreate):
    return {"name": user.name, "email": user.email, "age": user.age}



