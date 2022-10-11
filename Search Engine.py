"""
You are given few sentences as a list (Python list of sentences). Take a query string as an input
from the user. You have to pull out the sentences matching this query inputted by the user in
decreasing order of relevance after converting every word in the query and the sentence to lowercase.
The most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:

Please input your query string

“Python is”
Output:

3 results found:

    python is not python snake
    python is good
    Python is cool

"""
import re
str1 = input("Enter a string or sentence: ")
lst = []
n = int(input("Enter the number of elements in list"))
for i in range(n):
    elem = input("Enter the string element")
    lst.append(elem)

matches = 0
for i in range(len(lst)):
    temp = re.findall(str1, lst[i])
    lst.sort(key=lambda x: x.count(str1), reverse=True)
    matches = matches + lst[i].count(str1)

print(f"{str1} matches {matches} times in the list of strings")
print(f"The string list in descending order based on matches count: {lst}")
