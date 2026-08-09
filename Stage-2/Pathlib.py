# from pathlib import Path

# # def write_and_read(filename: str, message: str) -> str:
# #     # Write 3 lines here
# #     name = Path(filename)
# #     name.write_text(message)
# #     content = name.read_text()
# #     return content

# # if __name__ == "__main__":
# #     result = write_and_read("test.txt", "Backend Engineering")
# #     print(f"Result: {result}")
# #     assert result == "Backend Engineering"
# #     print("Micro-task 1 passed!")




# def append_log(filepath: Path, log_message: str) -> None:
#     # Write 2 lines here
#     with open(filepath,"a", encoding = "utf-8") as f:
#         f.write(f"{log_message}\n")
    


# if __name__ == "__main__":
#     log_file = Path("server.log")
    
#     # Clean up previous file if exists
#     if log_file.exists():
#         log_file.unlink()

#     append_log(log_file, "[INFO] Started")
#     append_log(log_file, "[ERROR] DB Error")

#     content = log_file.read_text(encoding="utf-8")
#     print(f"File contents:\n{content}")

#     assert "[INFO] Started" in content
#     assert "[ERROR] DB Error" in content
#     print("Micro-task 2 passed!")

# """Use with open(filepath, "a", encoding="utf-8") as f:
# Write f"{log_message}\n" to the file."""

"""save_config(path: Path, data: dict) -> None: Open in "w" mode and call json.dump(data, f)
load_config(path: Path) -> dict: Open in "r" mode and return json.load(f)"""

import json
from pathlib import Path

def save_config(path: Path, data: dict) -> None:
    # 2 lines: open in "w" mode, json.dump(data, f)
    with open(path, "w", encoding = "utf-8") as f:
        json.dump(data,f)

def load_config(path: Path) -> dict:
    # 2 lines: open in "r" mode, return json.load(f)
    with open(path, "r",encoding = "utf-8") as f:
        content = json.load(f)
        return content

if __name__ == "__main__":
    cfg_file = Path("config.json")
    my_config = {"app": "AI Analyzer", "port": 8000}

    save_config(cfg_file, my_config)
    result = load_config(cfg_file)

    print(f"Loaded config: {result}")
    assert result["app"] == "AI Analyzer"
    assert result["port"] == 8000
    print("Micro-task 3 passed!")
