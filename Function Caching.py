"""
                                    Function Caching
It reduces the delay by storing the function results in cache
"""
import time
from functools import lru_cache

n1 = int(input("Enter maxsize: "))


@lru_cache(maxsize=n1)
def func(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    print("Calling")
    func(3)
    print("Calling Again")
    func(3)
    print("Called")
