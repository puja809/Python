"""
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome
corresponding to that number.
Your first input should be the number of test cases and then take all the cases as input from the user.

Input:

3

451

10

2133
Output:

Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222
"""


def is_palindrome(n1):
    """
    This Function checks if a number is palindrome or not
    :param n1: number
    :return: True of False
    """
    rem = 0
    temp = n1
    while temp != 0:
        num = temp % 10
        rem = rem * 10 + num
        temp = temp//10
    if rem == n1:
        return True
    else:
        return False


choice = int(input("Enter the number of test cases you want to check: "))
for i in range(choice):
    n = int(input("Enter a number"))
    temp1 = n
    while True:
        if is_palindrome(n) is True:
            break

        else:
            n = n + 1

    print(f"The next palindrome of {temp1} is {n}")
