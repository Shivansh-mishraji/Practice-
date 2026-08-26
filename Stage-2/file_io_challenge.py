"""Write a function process_user_data(username: str, age: int, skills: list[str]) -> dict:

Create a directory user_storage if it doesn't exist (using Path).
Save a JSON file named user_storage/{username}.json containing {"name": username, "age": age, "skills": skills} using with open(..., "w") and json.dump().
Read that JSON file back from disk using with open(..., "r") and json.load().
Return the loaded dictionary."""
from pathlib import Path
import json

def process_user_data(username: str, age: int, skills: list[str]) -> dict:
    path = Path("user_storage")
    path.mkdir(parents = True, exist_ok = True)
    file_path = path / f"{username}.json"
    with open(file_path, "w", encoding = "utf-8") as f:
        data = {"name": username, "age": age, "skills": skills}
        json.dump(data,f)
        
    with open(file_path, "r", encoding = "utf-8") as f:
        content = json.load(f)
        return content

if __name__ == "__main__":
        p = process_user_data("Shivansh", 21, ["Python", "FastAPI"])
        assert isinstance(p, dict)
        assert p["name"] == "Shivansh"
        print("stage cleared")

