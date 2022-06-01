"""
                                Comprehensions
These provide an alternative syntax for creating list, set, dictionary and generators.
This increases code readability
"""
# List Comprehension
print("---------Lists---------")
lst = [i for i in range(10) if i % 5 == 0]
print(lst)

# Dictionary Comprehension
print("---------Dictionary---------")
dicts = {i: f"Items-{i}"for i in range(5)}
print(dicts)
# Reversing the dictionary with comprehension
dicts = {value: key for key, value in dicts.items()}
print(dicts)

# Set Comprehension
print("---------Sets---------")
sets = {i for i in ["Pu-ja", "Dia", "Jit"]}
print(sets)

# Generator comprehension
print("---------Generators---------")
evens = (i for i in range(100) if i % 2 == 0)
for i in evens:
    print(evens.__next__())
