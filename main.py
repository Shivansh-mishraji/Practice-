"""
=================================================================
 🚀 File: main.py
 ✨ Purpose: Advanced Machine Learning Operations and Processing
 📅 Last Updated: 2026
=================================================================
"""

# Main script to list files and folders in the current directory using pathlib
from pathlib import Path

# ==================================================
# Function Definition
# ==================================================
def readfileandfolder():
    path=Path("")
    items = list(path.glob("*"))
    for i,item in enumerate(items):
        print(f"{i+1} : {item} ")
print(readfileandfolder())