"""
                                 Class Methods in Python

With the help of class methods we can modify class variables through their instances as well.
Class methods can also be used as alternative constructors.
"""


class Employee:
    leaves = 19

    @classmethod
    def newleaves(cls, new):
        cls.leaves = new

    # Constructor
    def __init__(self, name, salary, leaves):
        self.name = name
        self.salary = salary
        self.leaves = leaves

    # Methods
    def details(self):
        return f"{self.name}'s salary is {self.salary}. He/She has {self.leaves} leaves"

    @classmethod
    def dash(cls, str):
        params = str.split("-")
        return cls(params[0], params[1], params[2])


Puja = Employee("Puja", 120000, 56)
print(Puja.details())
# print(Puja.__dict__)
Diya = Employee.dash("Diya-140000-23")
print(Diya.details())
