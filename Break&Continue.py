"""
                        Break and continue statement in python

Note:  Break statement helps to break a loop and come out of it where as continue statement helps
to skip iterations and continue from next
"""

# Write a code to print from 1 to 45 but break if its 44 and start printing from 5

i=1
while(1):
    if(i < 5):
        i=i+1
        continue
    print(i)
    i = i + 1
    if(i==44):
        break
