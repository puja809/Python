"""
                              Enumerate Function in Python

This function helps to iterate the indexes along with the items.
"""
# Print the list without the subject 'Maths'
lst = ["Biology", "Maths", "Physics", "Chemistry", "English"]
for index, item in enumerate(lst):
    if index == 1:
        continue
    print(item)
    index += 1

