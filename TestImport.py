def add(a, b):
    # int(input("Enter number 1: "))
    # int(input("Enter number 2: "))
    result = a+b
    return result


def sub(a, b):
    results = a-b
    return results


# Anything written inside main wont be executed when the program is imported
if __name__ == '__main__':
    print(add(2, 5))
    print(sub(45, 40))
