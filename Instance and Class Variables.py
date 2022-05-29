"""
Class variables: These are shared by all the instances of the class and can be modified by the class itself
Instance Variable: These are instance/objects own attributes
"""


class Employee:
    leaves = 12
    pass


Puja = Employee()
Purna = Employee()
Puja.job = "Engineer"
Purna.job = "Developer"
print(Puja.job, Puja.leaves)


# class variables can be modified by class only
Employee.leaves = 19
# This will not modify the class variables but will create an attribute for instance Puja
Puja.leaves = 30
print(Puja.__dict__)
print(Purna.__dict__)

print(Puja.job, Puja.leaves, Purna.leaves)
