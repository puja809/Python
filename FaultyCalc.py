"""
Design a faulty calculater. Below calculations will be calculated wrong:
45*3=555, 56+9=77, 56/6=4
Other calculations should be correct
"""

# User input 2 numbers and the operator:
num1=int(input())
num2=int(input())
opt=input()
# Logic for Faulty Calculator:
if opt=='*':
    if num1==45 or num2==45 and num1==3 or num2==3:
        print(555)
    else:
        print(num1*num2)
elif opt=='+':
    if num1==56 or num2==56 and num1==9 or num2==9:
        print(77)
    else:
        print(num1+num2)
elif opt=='/':
    if num1==56 and num2==6 :
        print(4)
    else:
        print(num1/num2)
elif opt=='-':
    print(num1-num2)