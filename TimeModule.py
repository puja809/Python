"""                                Time Module in Python
"""
import time

# To get the execution time of a program
init = time.time()
for i in range(5):
    print("Puja")
    # stops the program for 1 sec
    time.sleep(1)
print(time.time()-init)

init = time.time()
i=1
while i<=5:
    print("Diya")
    # stops the program for 1 sec
    time.sleep(1)
    i+=1
print(time.time()-init)


# Printing the local time:
print(time.asctime(time.localtime(time.time())))

