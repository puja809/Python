"""                                    Functions In Python

Functions are of 2 types in Python:
1. Built-in: already present, which we can call in our program
2. User-defined: Created by User
"""
# Built-in Function:
# Sum() function
# a = 50
# b = 40
# print(sum((a, b)))
# User Defined even or odd function:


def even(a):

    """This function will check if a given number is even or not"""
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Function docString tells us abut the function. It is a comment inside the function written for readability
print(even.__doc__)

print(even(int(input("Enter a number "))))

