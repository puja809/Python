import pickle
file = "iris.data"
f = open(file, "r")
main = f.read().split("\n")
filePickle = "Iris.pkl"
Obj = open(filePickle, "wb")
pickle.dump(main, Obj)
Obj.close()
f.close()


filePickle = "Iris.pkl"
Obj = open(filePickle, "rb")
pick = pickle.load(Obj)
print(pick)

