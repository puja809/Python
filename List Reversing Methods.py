"""
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted,
 based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

    Inbuilt method of python
    List name [::-1] slicing trick
    Swap the first element with the last one and second element with second last one and so on like,

[6 7 8 34 5] -> [5 34 8 7 6]

Input:

Take a list as an input from the user

[5, 4, 1]
Output:

[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!
"""

# lst = [1, 5, 6, 7, 89, 34]
print("Start entering the numbers for your list")
size = int(input("Enter the size of the list"))
lst = []
for i in range(size):
    lst.append(int(input("Enter the list element: ")))

# reverse method when applied on copied method reverses the original list as well. Hence, we used lst[:]
lst1 = lst[:]
lst1.reverse()
print(f"The reversed list using reverse method: {lst1}")

# slicing of list to reverse it
lst2 = lst[::-1]
print(f"The reversed list using slicing method: {lst2}")

# swapping of numbers to reverse the list.
for i in range(len(lst)//2):
    lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
print(f"The reversed list using swapping method: {lst}\n")

if lst1 == lst2 == lst:
    print("All methods give same result")
