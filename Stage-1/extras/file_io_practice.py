import json
from pathlib import Path
from typing import Union

# --- Level 1: Basic ---
def append_log_entry(log_file: Path, level: str, message: str) -> None:
    # Your code here
    pass

# --- Level 2: Intermediate ---
def load_or_create_config(config_path: Path, default_config: dict) -> dict:
    # Your code here
    pass

# --- Level 3: Advanced ---
def summarize_directory(dir_path: Path) -> dict[str, Union[int, list[str]]]:
    # Your code here
    pass

if __name__ == "__main__":
    base_dir = Path("stage2_storage/practice")

    # --- Test Level 1 ---
    log_path = base_dir / "logs" / "app.log"
    append_log_entry(log_path, "info", "Server started")
    append_log_entry(log_path, "error", "Database connection lost")
    assert log_path.exists()
    content = log_path.read_text(encoding="utf-8")
    assert "[INFO] Server started" in content
    assert "[ERROR] Database connection lost" in content
    print("✅ Level 1 Passed!")

    # --- Test Level 2 ---
    cfg_path = base_dir / "config" / "settings.json"
    default_cfg = {"app_name": "AI Analyzer", "port": 8000, "debug": True}
    
    # First call creates the file with defaults
    res1 = load_or_create_config(cfg_path, default_cfg)
    assert res1["port"] == 8000
    assert cfg_path.exists()

    # Second call reads existing file
    res2 = load_or_create_config(cfg_path, {"port": 9000})
    assert res2["port"] == 8000  # Should return original saved 8000, NOT 9000
    print("✅ Level 2 Passed!")

    # --- Test Level 3 ---
    summary = summarize_directory(base_dir)
    assert summary["total_files"] >= 2  # app.log & settings.json
    assert summary["total_dirs"] >= 2   # logs/ & config/
    assert ".json" in summary["extensions"]
    assert ".log" in summary["extensions"]
    print("✅ Level 3 Passed!")

    print("\n🎉 ALL LEVELS PASSED!")
