"""
Note:

Iterable - __iter__ : Any object that can iterated like a string, list
Iterator - __next__ : Helps in iterating an object
Iteration - The process of iterating an object
Generator - It generated numbers during the process. Its advantage is that it generated during the execution
hence saves memory. Generator can be iterated only once
"""


def gen(n):
    for i in range(n):
        yield i


n = gen(3)
print(n.__next__())
print(n.__next__())
print(n.__next__())

# string is iterable as it has __iter__ method defined
st = "FOREST"
for i in st:
    print(i)

st1 = "123456789"
it = iter(st1)
for i in st1:
    print(it.__next__())
    