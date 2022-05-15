"""
Scope of a variable: It defines where the variable is accessible
"""

# Global variable:
x = 10


def scopes():
    # Local Variable
    x = 40
    print("Local Variable ", x)


scopes()

print("Global Variable", x)

"""
Note: To give access to a global variable to a function we use the keyword 'global'
"""


def change():
    global x
    x = x+20
    print("Accessed global variable", x)


change()
