# set: A data structure in Python that allows only unique values. We can create set using lists

s=set({1,2,2})
# print(type(s))
# Adding objects to the set
s.add(3)
# Creating sets from list
lst=["Puja","Diya",1,2]
s1=set(lst)
# Union of 2 sets
s2=s.union(s1)
# Intersection of 2 sets
s3=s.intersection(s1)
print(s2)
print(s3)