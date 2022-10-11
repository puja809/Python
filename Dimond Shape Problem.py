"""
Note: Multiple Inheritance results in Dimond shape problem and creates confusion
hence it is advised not to use Multiple inheritance. Although Python resolves this issue but c++
doesn't. Java does not allow multiple inheritance
"""


class A:
    @staticmethod
    def met():
        return "I am method in A"


class B(A):
    @staticmethod
    def met():
        return "I am method in B"
    pass


class C(A):
    @staticmethod
    def met():
        return "I am method in C"
    pass


class D(B, C):
    @staticmethod
    def met():
        return "I am method in D"
    pass


a = A()
b = B()
c = C()
d = D()

print(d.met())

"""
Note: Class D will first search for the method in itself, then inside B, 
then with C and at last within A
"""