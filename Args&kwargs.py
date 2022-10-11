"""
                                  Args and Kwargs

Note: If we add normal argument in a function to pass a list or tuple, later we try adding new elements to
the list,it will throw error. args and kwargs allow us to add new elements to the list
without changing the function argument.

args and kwargs are optional
"""


# Normal function:
# def norm(a,b):
#     print(a,b)
#
#
# norm("Puja", "Diya", "Dona")

"""The above error in norm function can be avoided using agr and kwarg"""


def arg_kwarg(normal, *arg, **kwarg):
    print(normal)
    for items in arg:
        print(items)
    for key, values in kwarg.items():
        print(f"{values} is a {key}")


item = ["Biology", "Physics", "English", "Maths"]
dicts = {"Doctor": "Dora", "Engineer": "Puja", "HR": "Dona", "Student": "Diya"}
arg_kwarg("Lets write code\n", *item, **dicts)
