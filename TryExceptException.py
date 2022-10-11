"""Try except Exception in Python"""

a = input("Enter a number\n")
b = input("Enter a number\n")

try:
    print("The sum of the numbers is ", int(a)+int(b))
except Exception as error:
    print(error)

print("Got the error")
