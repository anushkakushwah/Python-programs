students = [45,65,76,65,34]
length=len(students)
update=n=int(input("Enter marks to update"))
for i in range(0,length):
    if students[i]==update:
        students[i]=int(input("Enter new marks"))
print("students length", len(students))
update=n=int(input("Enter marks to update"))
for i in range(0,length):
    if students[i]==update:
        students[i]=int(input("Enter new marks"))
print(students)
