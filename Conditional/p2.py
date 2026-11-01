#to ask user for the marks and giving if they pass or fail
m1= int(input("Enter the marks of sub 1:"))
m2 = int(input("Enter the marks of sub 2:"))
m3= int(input("Enter the marks of sub3:"))
m4= int(input("Enter the marks of sub4: "))
m5 = int(input("Enter the marks of sub5:"))
total = m1+m2+m3+m4+m5
percentage = (total/500)*100
if percentage>33:
    print("Student passed.")
else:
    print("Student failed.")
