students=[]
n=int(input("enter no of students :"))
for i in range(n):
    print("Enter marks ",i+1)
    m=int(input())
    students.append(m)
print(students)
print("Total no of marks",students)
print("maximum no of marks",max(students))
print("minimum no of marks",min(students))
total=sum(students)
noofstudents=len(students)
avg=total/noofstudents
print("average no of marks",avg)

# rem=n=int(input("Enter marks to delete"))
# if rem in students:
#     students.remove(rem)
# else:
#     print("marks not exist")
# print(students)

# search=n=int(input("Enter marks to search"))
# if search in students:
#     print(search,"found")
# else:
#     print("marks not exist")
# print(students)

length=len(students)
update=n=int(input("Enter marks to update"))
for i in range(0,length):
    if students[i]==update:
        students[i]=int(input("Enter new marks"))
        break
print(students)