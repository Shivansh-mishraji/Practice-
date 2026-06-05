"""
=================================================================
 🚀 File: task2.py
 ✨ Purpose: Advanced Machine Learning Operations and Processing
 📅 Last Updated: 2026
=================================================================
"""

# Script for parsing data files and handling exceptions during type conversion

"""Phase 2: Intermediate (Data Parsing and Type Handling)
Now, let's introduce messy data that causes internal crashes.
The Task: Assume your raw_data.txt contains rows of comma-separated numbers representing feature data (e.g., 12.5, 4.2, 9.8). However, some rows are corrupted with text (e.g., 12.5, error, 9.8). Parse the file line by line, convert the values to floats, and calculate the sum of each row.
File Handling Focus: Append valid rows to clean_data.csv and append bad rows to a separate error_log.txt.
Try-Except Focus: * Use a try-except block inside your loop to catch ValueError when Python tries to convert a word into a float.
Introduce the else block (runs only if the try block succeeds) to write to the clean file.
The Goal: The script processes the entire file. Valid rows are saved, and whenever a ValueError triggers, the exact row and a custom error message are logged into the error file without stopping the loop."""


# ==================================================
# Function Definition
# ==================================================
def readfile(filename):
    try:
        with open(f"{filename}.txt","r") as f:
            items=content=f.readlines()
            print(content)
            

    except Exception as err:
        print(f"an error accured as {err}")

    else :
        total_sum = 0

        
        for item in items:
            try:
                cleaned=float(item)
            except ValueError:
                continue
            else:
                total_sum +=cleaned
        print(total_sum)
name = input("Enter file Name : ")
readfile(name) 