"""
                        Find the factorial of a number
"""

n = int(input("Enter a number: "))
result = 1
if n < 0:
    print(f"Please give a positive number")
elif n == 0:
    print(f"The factorial of {n} is 0")
else:

    for i in range(1, n+1, 1):
        result = result*i

    print(f"The factorial of {n} is {result}")
