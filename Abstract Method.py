"""
Abstract Base class: It implies certain rules on the child classes by using abstract methods
Note: Base class cannot have its objects or instances
"""
from abc import ABCMeta, abstractmethod


# The base class imposes the rule to create a printarea method in it every child class
class Base(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Base):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def printarea(self):
        return self.length * self.breadth
    pass


Rect = Rectangle(6, 7)
print("The area of rectangle is", Rect.printarea())
