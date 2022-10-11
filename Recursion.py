"""
Recursion: When a function calls itself.
"""

# Factorial of a number using iterative method


def fact_iterative(n):
    fact = 1
    for i in range(1, n+1, 1):
        fact = fact*i
        # i = i+1
    print(fact)


num = int(input("Enter a number for iterative factorial: "))
fact_iterative(num)


def fact_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*fact_recursive(n-1)


num = int(input("Enter a number for Recursion factorial: "))
print(fact_recursive(num))
