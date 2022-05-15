"""
With block in Python allows us to open and close a file. We do not have to close a file explicitly.
We can perform all file handling operations within a with block
"""
with open("ReadingWithPython.txt", "rt") as f:
    print(f.read())
