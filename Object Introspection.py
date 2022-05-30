"""
Object Introspection: Getting the details of an object like its type, id, associated methods/functions etc
object introspection can be done using type(), id(), dir(), inspect module
"""
import inspect


class Employee:
    pass


class Student:
    pass


print(type(Employee))
print(id(Student))
print(dir(Student))
print(inspect.getmembers(Employee))