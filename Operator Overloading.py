"""
Operators Overloading: Providing extended meaning to the operators other than their basic operation
Dunder Methods: Special methods like __add__
"""


class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    # This dunder method returns a string when a class instance is printed
    def __repr__(self):
        return f"Employee({self.name},{self.job}, {self.salary})"

    # This dunder method performs operator overloading on + operator
    def __add__(self, other):
        return self.salary + other.salary

    # This dunder method returns a string when a class instance is printed
    """Note: __str__ has more priority over __repr. If no __str__ method is there __repr__ will replace 
    __str__"""
    def __str__(self):
        return f"{self.name} is {self.job}. Her salary is {self.salary}"


Dora = Employee("Dora", "Doctor", 100000)
Dona = Employee("Dona", "Engineer", 200000)
print(Dora)
print(Dona)
print(Dona + Dora)
