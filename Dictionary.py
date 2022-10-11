#  Dictionary is key value pairs

d1={"Puja":"Python",
    "Krushna":"Docker",
    "Diya":"Biology",
    "Dora":"MBBS"

}
# copy dictionary to a new dictionary
# Any changes Made in the copy dictionary will not affect the main dictionary
d2=d1.copy()
d2.update({"Purna":"PL/SQL"})
# Deleting one key from dictionary
# del d2["Puja"]
# adding new value to the dictionary without using the update function
d2["Puja"]="Python"
# print(d2)
print(d2.keys())
print(d2.items())
# print(d1)
# print(type(d1)) : <class 'dict'>
