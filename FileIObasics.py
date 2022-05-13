"""                                    File I/O Basics

Note:
    1. "r" - Opens file for reading (default mode)
    2. "w" - Opens file for writing
    3. "x" - Creates file if it does not exist
    4. "t" - Opens file in text mode (default mode)
    5. "b" - Opens file in binary mode
    6."+" - Opens file for both raed and write
    7. "a" - adding more content to the existing file
"""


"""                           Reading a file                           """

# Create a pointer to the file we want to read:

# Note: If you open a file make sure to close it after use so that all resources are free.
f = open("ReadingWithPython.txt", "r")

# read() function allows us to read a file
# content = f.read()
# print(content)

# To read specific characters from a file:

# content = f.read(3)
# print(content)
#
# content = f.read(3)
# print(content)
"""
Note: Python will not allow us to read the characters that has been read again. It will start
reading from the next characters
"""

# Reading a file One line at a time:
# print(f.readline())
# print(f.readline())
# print(f.readline())

# Iterating a file:
for line in f:
        print(line, end="")

# Reading a file and storing each line in a list
# print(f.readlines())

