"""
                                    Super() and Overriding
"""


class Dad:
    # class variable
    game = "Cricket"

    def __init__(self):
        # instance variable
        self.game = "Chess"
        pass


class Son(Dad):
    game = "Baseball"

    def __init__(self):
        super().__init__()
        self.game = "Basketball"
        pass

# created an instance of class Son


"""
Note-1: First preference is given to instance variable of the class itself, then super class instance variable,
then class variable and at last super class variable

Note-2: Once a method or attribute is override the child class will use the override method or attribute
"""
son = Son()
dad = Dad()
print(son.game)
print(dad.game)
