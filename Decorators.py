"""
Decorators in Python: These are used to modify the functionality of a function
"""


def decorator_func(func):
    def exec1(a):
        print("Hi! I am a decorator")
        func(a)
        print("My job is to modify a function")
    return exec1


@decorator_func
def mul(a):
    print(a*a)


mul(9)
