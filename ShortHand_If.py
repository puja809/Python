"""                                 Short-Hand If-Else in Python                               """

a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))

# if a > b:print("a is greater than b")

# If else in one statement> But this will reduce readability
print("a is greater than b") if a>b else print("a is lesser than b")
