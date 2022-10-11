"""                         Writing, appending and updating a file       """

# Opening the file in write mode will delete the content of the existing file and update it with new content
# f = open("ReadingWithPython.txt", "w")
# content = f.write("Hello I am Puja")

# Opening the file in append mode will add the new content with existing content
# f = open("ReadingWithPython.txt", "a")
# content = f.write("\nI am learning Python\n")


# Opening the file in read and write mode will allow us to read and write the file at same time
f = open("ReadingWithPython.txt", "r+")
content=f.write("\nHi all!\n")
f.close()
f = open("ReadingWithPython.txt", "r+")
print(f.read())
f.write("Thank You")