"""
                    How to get the execution time of a code:
"""

import time

initial = time.time()
# print(f"The initial time is {initial}")


def sums(a, b, c):
    return f"The sum of {a}, {b} and {c} is {a + b + c}"


if __name__ == '__main__':
    n1 = int(input("Enter 1st Number"))
    n2 = int(input("Enter 2nd Number"))
    n3 = int(input("Enter 3rd Number"))
    print(sums(n1, n2, n3))
    print(f"The time taken by the code is {time.time() - initial}")
