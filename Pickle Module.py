import pickle

# Creating a binary file or pickling

# fruits = ["Apple", "Mango", "Orange", "Strawberry", "Banana", "Guava"]
# file = "fruitsData.pkl"
# fruitsObj = open(file, 'wb')
# pickle.dump(fruits, fruitsObj)
# fruitsObj.close()


# Reading the pickles file
file = "fruitsData.pkl"
fileObj = open(file, 'rb')
pick = pickle.load(fileObj)
print(pick)

