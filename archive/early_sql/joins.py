import sqlite3

def setup_database():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE resumes (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            filename TEXT NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    
    # Insert sample data
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?);", [
        (1, "Shivansh", "shivansh@example.com"),
        (2, "Aarav", "aarav@example.com"),
        (3, "Priya", "priya@example.com") # Priya has no resume
    ])
    
    cursor.executemany("INSERT INTO resumes VALUES (?, ?, ?, ?);", [
        (101, 1, "shivansh_resume.pdf", 85),
        (102, 2, "aarav_resume.pdf", 92)
    ])
    
    conn.commit()
    return conn

# --- YOUR TASK: Write the SQL query strings ---

def get_inner_join_query() -> str:
    """Return SQL string for INNER JOIN between users and resumes on matching user_id.
    Select: users.name, resumes.filename, resumes.score"""
    # Replace with your SQL string
    return """
        SELECT users.name, resumes.filename, resumes.score
        FROM users
        INNER JOIN resumes ON users.id = resumes.user_id
    """

def get_left_join_query() -> str:
    """Return SQL string for LEFT JOIN from users to resumes on user_id.
    Select: users.name, resumes.filename"""
    # Replace with your SQL string
    return """
        SELECT users.name, resumes.filename
        FROM users
        LEFT JOIN resumes ON users.id = resumes.user_id
    """

if __name__ == "__main__":
    db = setup_database()
    cursor = db.cursor()

    # Test INNER JOIN
    inner_results = cursor.execute(get_inner_join_query()).fetchall()
    print("INNER JOIN Output:", inner_results)
    assert len(inner_results) == 2  # Priya excluded because no resume
    assert inner_results[0][0] == "Shivansh"

    # Test LEFT JOIN
    left_results = cursor.execute(get_left_join_query()).fetchall()
    print("LEFT JOIN Output:", left_results)
    assert len(left_results) == 3   # Priya included with None for filename!
    assert left_results[2] == ("Priya", None)

    print("\n🎉 SQL Day 1 JOINs Passed!")
