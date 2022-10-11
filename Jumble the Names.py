"""
It's result day at school and not everyone is happy. You decided to make your friends laugh by
jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated by space as input.
Output should be funny names in the same order.

Input:

Enter number of friends:

3

Enter the name of your 3 friends:

Rohan Das

Shubham Agarwal

Ritesh Arora
Output:

Ritesh Das

Shubham Arora

Rohan Agarwal

Try to solve these new programming puzzles.

"""
import random
rnd1 = 0
rnd2 = 0
try:
    n = int(input("Enter the no. of names to be entered"))
    lst = []
    # Enter the names and add them to a list
    for i in range(n):
        name = input("Enter the names")
        lst.append(name)
    names = []
    fname = []
    lname = []
    # Split the list based on spaces and add first & last name to separate lists
    for i in range(len(lst)):
        names.append(lst[i].split(" "))
        fname.append(names[i][0])
        lname.append(names[i][1])
    # Select random first and lat names from the respective lists
    for i in range(len(names)):
        print(f"{random.choice(fname)} {random.choice(lname)}")

except Exception as error:
    print(error)
