"""Phase 1: The Basics (Read, Write, and Missing Files)
Start by handling basic file operations and the most common file error.
The Task: Create a script that attempts to open a file called raw_data.txt and read its contents. Write those contents into a new file called processed_data.txt.
File Handling Focus: Use the with open(...) context manager to ensure files close automatically.
Try-Except Focus: Wrap your opening logic in a try-except block to catch a FileNotFoundError.
The Goal: If raw_data.txt doesn't exist, your script shouldn't crash with a giant red error traceback. Instead, it should politely print: "Error: The target dataset could not be found. Please check the directory."""


def createfile(new,data):
    try:
        with open (f"{new}.txt" , "x") as file:
            file.write(f"{data}")
    except Exception as err:
        print(f"An error accured as {err}")
    else:
        print("File created and written succcessfully.")

def readfile(): 

    file = input(" Enter file name to read : ")
    try:
        with open(f"{file}.txt", "r") as f:
            content = f.read()
            print (content)
        
    except Exception as err:
        print(f"An error accured as {err}")
    else:
        
        print("File read succcessfully.")
        new = input("Enter new file name : ")
        createfile(new,content)
    finally : 
        print("task completed sucessfully. ")

readfile()