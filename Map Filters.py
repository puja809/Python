"""
Map-function in Python: It is used to apply a function on a list of object
"""

# Mapping in-built function:
lst = ["45", "56", "79"]
lst = list(map(int, lst))
for i in range(len(lst)):
    lst[i] = lst[i]+5
print(lst)


# Mapping user-defined function:
def sq(a):
    return a*a


print(list(map(sq, lst)))


# Mapping a list of function:
def cube(a):
    return a*a*a


func = [sq, cube]
number = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(number)):
    number = list(map(lambda x: x(i), func))
    print(number)

"""
Filter function helps us to filter elements from a given list based on a function
"""

print("*************Filter************")


def greater_5(num):
    if num > 5:
        return "true"


lst1 = [1, 3, 8, 10, 111, 89, 56]
lst1 = list(filter(greater_5, lst1))
print(lst1)

"""
Reduce function from functools perform cumulative operations
"""

print("-----------------Reduce-------------------")

from functools import reduce
lst2 = [1, 2, 3, 4]
num = reduce(lambda x, y: x*y, lst2)
print(num)
