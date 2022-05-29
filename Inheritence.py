"""
Inheritance: It allows to inherit the functionalities of an existing class
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


class Programmer(Employee):
    def __init__(self, name, salary, leaves, prog):
        super().__init__(name, salary, leaves)
        self.prog = prog


rohan = Programmer("Rohan", 300, 34, 'Python')
print(rohan.prog)
