from pathlib import Path

def readfileandfolder():
    path=Path("")
    items = list(path.glob("*"))
    for i,item in enumerate(items):
        print(f"{i+1} : {item} ")
print(readfileandfolder())