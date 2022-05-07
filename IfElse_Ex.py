"""Input: user's age
Output: age< 18 then cannot drive
        age>18 then can drive
        age=18 Computer cannot decide"""

print("Enter Your Age Please!!")
age=int(input())
if age>100:
    print("Please Enter a valid Human age!!!")
elif age>18:
    print("Wow!!You can drive now")
elif age<18:
    print("Oh noo!!You are not eligible to drive")
else:
    print("Sorry! Computer cannot decide")
