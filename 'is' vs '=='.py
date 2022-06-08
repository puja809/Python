"""
    1. '==' refers to the value of the object
    2. 'is' refers to the same object with different references
"""

a = b = [2, 3, 4, 5]
c = [2, 3, 4, 5]
# Comparing the value
print(a == b)
# a and b refers to same object
print(a is b)

# a and c has same value
print(a == c)
# a and c refers to different object
print(a is c)
