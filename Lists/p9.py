# list=[45,67,89]
# print(list)
# print(type(list))
# l1=[12,"ayush ",657.89]
# print(l1[0])
# print(l1[1])
# print(l1[2])
# students=["Ayush","Dharmesh","Jay"]
# print(students)
# for i in students:
#     print(i)
# print("Aadi" in students)
# students.append("Aadi")
# print(students)
# if "Treesa" not in students:
#     students.append("Treesa")
# else:
#     print("Duplicate")
# print(students)
# students.insert(0,"Akshay")
# print(students)
# l1=[12,34,45,6,78,89]
# l2=[23,34,56,78,90]
# # print(len(l1))
# print(max(l1))
# print(min(l1))
# print(sum(l1))
# l2=l1
# l2.sort()
# l2=sorted(l1)
# print(l1)
# print(l2)
# l3=l1+l2
# print(l1)
# print(l2)
# print(l3)
# l1.append(12)
# print(l1)
# l1.append([13,45,67])
# print(l1)
# print(l1[4])
# print(l1[5])


# l2.extend([55,67,89])
# # print(l2)

# l1=[12,34,45,6,78,89,12,12,12]
# l2=[23,34,56,78,90]
# print(l1+l2)
# print(l1*3)
# print(l1.count(12))

list=[12,34,45,6,78,89,13,14,12]
# print(list)
# print(list[2:])
# print(list[:6])
# print(list[2:8:2])
# print(list[-2:-1])
# 
# hw without using second variable remove the duplicate\

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