"""
Multiple Inheritance: A class will inherit from multiple classes
"""


class Employee:
    # constructor
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    # Method
    def details(self):
        return f"{self.name}'s salary is {self.salary}. She works as {self.job}"


# Dora = Employee("Dora", "Doctor", 12000)
# print(Dora.details())

class Programmer:
    @staticmethod
    def prog(prog):
        return f"{prog} expert"


# Multiple Inheritance
class CoolDude(Employee, Programmer):
    def det(self):
        return f"{self.name}'s salary is {self.salary}. She works as {self.job}."


Puja = CoolDude("Puja", "Engineer", 130000)
print(Puja.det(), " She is a", Puja.prog("Python"))
