from pathlib import Path

def write_and_read(filename: str, message: str) -> str:
    # Write 3 lines here
    name = Path(filename)
    name.write_text(message)
    content = name.read_text()
    return content

if __name__ == "__main__":
    result = write_and_read("test.txt", "Backend Engineering")
    print(f"Result: {result}")
    assert result == "Backend Engineering"
    print("Micro-task 1 passed!")
