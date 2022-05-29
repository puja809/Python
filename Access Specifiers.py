"""
Access Specifiers:
1. Public - Any class can access
2. Private - Only main class has the access
3. Protected - The main class and child classes has the access

Note: Python handles private attributes with name mangling.
It saves the private variables along with class name

"""


class Electronics:
    # Public
    sub1 = "Maths"
    sub2 = "Economics"
    # Protected
    _sub3 = "Digital Electronics"
    # Private
    __sub4 = "MPMC"

    @property
    def sub3(self):
        return self._sub3


print(Electronics.sub2)


print(Electronics._sub3)


print(Electronics._Electronics__sub4)
