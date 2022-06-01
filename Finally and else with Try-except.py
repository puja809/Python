"""
Finally: Its is the part of the code that will always run despite try or exception. It is used for code
clean-up
Else: Else statement will only run if exception is not occurring
"""

try:
    f = open("DrinkWater-Log.txt")
except Exception as e:
    print(e)
else:
    print("Exception not occurred")
finally:
    try:
        f.close()
    except Exception as e:
        print(e)

