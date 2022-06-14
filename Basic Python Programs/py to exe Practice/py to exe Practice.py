"""
1. Write a code to find all dividers of a number.
2. Convert this file to exe
3. generate only one .exe file
"""

n = int(input("Enter a number: "))
lst = []
for i in range(1, n+1, 1):
    if n % i == 0:
        lst.append(i)

print(f"The divider list of {n} is: {lst}")
a = input()
