"""
                                Multi-Level Inheritance
"""


class Dad:
    game = "Basketball"


class Son(Dad):
    @staticmethod
    def details():
        return f"Son plays {Dad.game}"


class Grandson(Son):
    # overriding the method inherited from class Son
    @staticmethod
    def details():
        return f"Grandson also plays {Dad.game}"


print(Grandson.details())
