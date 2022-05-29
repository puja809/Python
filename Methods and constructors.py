"""
Methods: Functions inside classes.
Constructors: allows classes to accept arguments and helps in code re-usability
"""


class Employee:
    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method
    def emp(self):
        return f"{self.name}'s salary is {self.salary}"


Dona = Employee("Dona", 100000)
Dona.name = "Dona"
Dona.salary = 100000
print(Dona.emp())

Dora = Employee("Dora", 200000)
print(Dora.name)
