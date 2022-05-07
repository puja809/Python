"""
Create a dictionary of 4 words which will take any of the 4 words as input from user and return the meaning
of the word 
"""

words={
    "set":"Collection of well-defined objects",
    "Mutable":"Anything that can change",
    "Immutable":"Anything that cannot change",
    "Python":"Programming language"
}
print("Please enter a word")
w=input()
print(words[w])
print("Thank you!!")