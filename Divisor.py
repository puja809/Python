"""
The task you have to perform is “Divide the Apples.”
This task consists of a total of 10 points to evaluate your performance.
Problem Statement:-

Harry Potter has got the “n” number of apples.
Harry has some students among whom he wants to distribute the apples.
These “n” number of apples is provided to harry by his friends,
and he can request for few more or a few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

Input:

Take input n, mn, and mx from the user.
Output:

Print whether the numbers between mn and mx are divisors of “n” or not.
If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.
Example:

If n is 20 and mn=2 and mx=5

2 is a divisor of20

3 is not a divisor of 20

…

5 is a divisor of 20
"""

try:

    n = int(input("Enter a number: "))
    min = int(input("Enter the minimum range"))
    max = int(input("Enter the maximum range"))

    if min > max:
        print("Minimum range should be less than maximum range")

    else:
        for i in range(min, max+1, 1):
            if n % i == 0 and min != max:
                print(f"{i} is a divisor of {n}")
            elif min == max:
                if n % i == 0:
                    print(f"{i} is a divisor of {n}. Min and max value cannot be equal")
                else:
                    print(f"{i} is not a divisor of {n}")

            else:
                print(f"{i} is not a divisor of {n}")

except Exception as e:
    print(e)
