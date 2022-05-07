"""
Take a list of different items. Print the list items only if:
The item is a number and greater than 6
"""

list=[1,2,5,3,"Orange","Lemon",'A',100,56,89,'E','I','O','U',"Watermelon",300,int]
for items in list:
    if type(items)==int and items>6:
        print(items)
