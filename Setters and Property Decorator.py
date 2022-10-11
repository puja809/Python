"""
                                        Setters and Property Decorators
    1. property decorator: It helps us to run the methods like attributes. For example printemail
    in below example
"""


class Employee:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname
        # self.email = f"{name}.{lname}@gmail.com"

    def details(self):
        return f"The employee is {self.name} {self.lname}"

    @property
    def email(self):
        if self.name is None or self.lname is None:
            return "No email!!"
        return f"{self.name}.{self.lname}@gmail.com"
        pass

    # setting the first name and last name through email
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.name = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.name = None
        self.lname = None


dora = Employee("Dora", "Ganguly")
dora.name = "Pranjali"
dora.email = "doodoo.googoo@yahoo.com"

print(dora.name)
del dora.email
print(dora.email)
