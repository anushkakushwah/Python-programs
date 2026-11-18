set = {12, "Siddharth", 07.88}
print(set)
print(type(set))
s1 = {11,22,33,44}
print(s1)
s1.add(55)  #to add one element
print(s1)
#to add more element
s1.update([77,88,99])
print(s1)
#to create empty set
s2 = {}
print(s2)
#to delete element in set
s1.remove(33)
print(s1)
#discard...if element no found will not give error
#remove..if element not found then it will give error
s1.pop()
print(s1)
#to make set empty
s1.clear()
set3 = s1.copy()
print(set3)
