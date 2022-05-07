"""
If Else statement in python is used to check various conditions inside a code
Note: If we use if instead of elif in all if else statements, python interpreter will check all the conditions
even after the desired condition is met, which is not a efficient way of coding.
"""

# Using in & not in operator in if else:

age = int(input())
lst = [10, 11, 12]

if age in lst:
    print("You will get a candy")
elif age not in lst and age<60:
    print("You will  get a Toffee")
elif age >= 60 and age < 100:
    print("You will get a coffee")
elif age>=100 and age :
    print("You will get a Cup of Tea")