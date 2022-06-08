"""
                                        Raise Keyword in Exception
"""

name = input("Enter your name: ")


if name.isnumeric() is True:
    raise Exception("Nane cannot be a number")

else:
    print(f"Hello {name}")


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num2 or num1 is 0:
    raise ZeroDivisionError("Number cannot be zero")
else:
    print(f"The division result is {num1/num2}")