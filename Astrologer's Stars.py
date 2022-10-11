n = int(input("Enter a Number "))
state = input("True or False ")
if state == "True":
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
elif state == "False":
    for i in range(n+1, 0, -1):
        for j in range(0, i-1):
            print("* ",end=" ")
        print("")

