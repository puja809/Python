"""
                            Check a number is palindrome or not
"""

try:
    n = int(input("Enter a number: "))
    temp = n
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n//10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

except Exception as error:
    print(error)
