"""
Continue taking input from user and printing till the input is greater than 100
"""

while(True):
    num = int(input("Enter a number "))
    if(num>100):
        print("Now the code will stop as you have given a input greater than 100")
        break;
    else:
        print("Try again!!\n")
        continue;


