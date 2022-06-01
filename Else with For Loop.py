"""
                                    Else with for loop
If the for loop ends normally without the interruption of break statement then the control will move to
else part. If the for loop ends by break then the else statement will not be executed
"""

veggies = ["Tomato", "Potato", "Cucumber", "Onion"]
for i in veggies:
    if i == "Carrot":
        print("Item Present")
        break

else:
    print("Item not found")
