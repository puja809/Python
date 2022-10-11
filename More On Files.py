f = open("ReadingWithPython.txt")
print(f.readline())
# To check the position of 'f' pointer
print(f.tell())
# Move the pointer to a particular position:
f.seek(0)

print(f.readline())
f.close()
