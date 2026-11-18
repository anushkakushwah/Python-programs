#  ---------------------Dictionary comprehension -------------------------


d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four"}

d2 = {i:i for i in range(1,11)}

d3 = {x:y for x,y in d1.items() if x%2==0}

print(d3)

l1 = ["Roll", "Name", "Marks"]
l2 = [12, "Jayesh", 63.22]

student = {l1[i]:l2[i] for i in range(len(l1))}

print(student)
print(student.keys())
print(student.values())