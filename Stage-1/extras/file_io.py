import json
from pathlib import Path

def ensure_dir(dir_path: Path) -> Path:
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path

def save_json(file_path: Path, data: dict) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_json(file_path: Path) -> dict:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_all_files(dir_path: Path, extension: str) -> list[Path]:
    return list(dir_path.glob(f"*{extension}"))

if __name__ == "__main__":
    test_dir = Path("stage2_storage/resumes")
    ensure_dir(test_dir)
    assert test_dir.exists()

    sample_resume = {
        "candidate": "Shivansh Mishra",
        "role": "Backend AI Engineer",
        "skills": ["Python", "FastAPI", "SQL", "Docker"]
    }

    file1 = test_dir / "resume_01.json"
    save_json(file1, sample_resume)
    assert file1.exists()

    loaded_data = load_json(file1)
    assert loaded_data["candidate"] == "Shivansh Mishra"
    assert "FastAPI" in loaded_data["skills"]

    files = get_all_files(test_dir, ".json")
    assert len(files) >= 1
    assert file1 in files

    print("All File I/O tests passed!")
