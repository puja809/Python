"""
                                 Statis Method
"""


class Student:
    @staticmethod
    def details(name, age):
        return f"{name}'s age is {age}"


print(Student.details("Puja", 24))
