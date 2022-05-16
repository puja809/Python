"""
Fibonacci Series:
1. Using iterative method (Series)
2. Using Recursive method (nth fibonacci number)
"""


def fib_iterative(n):
    f = 0
    f1 = 1
    print(f, end=",")
    print(f1, end=",")
    for i in range(n):
        temp = f + f1
        print(temp, end=",")
        f, f1 = f1, temp
        if temp == n:
            break


num = int(input("Enter a number for Iterative Method: "))
fib_iterative(num)


def fib_recursion(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)


num = int(input("\nEnter a number for Recursive Method: "))
print(fib_recursion(num))
