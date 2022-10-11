"""
Problem Statement:-

Take age or year of birth as an input from the user. Store the input in one variable.
Your program should detect whether the entered input is age or year of birth and
tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

    Do not use any type of module like DateTime or date utils. (-5 points)
    Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
    Your code should handle all sorts of errors like :            (2 points)

    You are not yet born
    You seem to be the oldest person alive
    You can also handle any other errors, if possible!

"""
year = int(input("Enter the year in which you want to get your age "))
current_year = int(input("Enter the current year "))
# result_age = 0
print("What you want to enter? ")
choice = input("Press A for age or D for Date Of Birth ")
if choice == 'A':
    age = int(input("Enter your age: "))
    if 150 >= age > 0:
        birth_year = current_year - age
        result_age = year - birth_year
        hundred = birth_year + 100
        if result_age <= 0:
            print(f"You were not yet born in {year}")
        else:
            print(f"Your age in {year} is {result_age}")
            print(f"You will turn hundred in the year {hundred}")
    elif age <= 0:
        print("Age cannot be negative or Zero!!")
    else:
        print("You seem to be the oldest person alive")

elif choice == 'D':
    dob = int(input("Enter Your DOB: "))
    if dob >= 0:
        result_age = year - dob
        hundred = dob + 100
        if result_age <= 0:
            print(f"You were not yet born in {year}")
        else:
            print(f"Your age in {year} is {result_age}")
            print(f"You will turn hundred in the year {hundred}")
    else:
        print("Date of Birth cannot be zero or negative!!!")
