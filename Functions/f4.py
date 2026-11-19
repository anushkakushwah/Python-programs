#To find graddes, taking input of marks
#WITHOUT PARAMETER, WITHOUT RETURN TYPE
def checkGrades():
    sub1= int(input("Enter marks of first subject :"))
    sub2= int(input("Enter marks of second subject :"))
    sub3= int(input("Enter marks of third subject :"))
    sub4= int(input("Enter marks of fourth subject :"))
    sub5= int(input("Enter marks of fifth subject :"))

    total = sub1 + sub2 + sub3 + sub4 + sub5
    per = (total/500)*100

    if per>=90 and per<=100:
        print("Grade A+")
    elif per>=80 and per<90:
        print("Grade A")
    elif per>=70 and per<80:
        print("Grade B+")
    elif per>=60 and per<70:
        print("Grade B")
    elif per>=50 and per<60:
        print("Grade C")
    elif per>40 and per<90:
        print("Grade D")
    else:
        print("Fail")

checkGrades()
print("-------------------------------------------------------------------------------------------")
#WITHOUT PARAMETER WITH RETURN TYPE
def checkGrades():
    sub1= int(input("Enter marks of first subject :"))
    sub2= int(input("Enter marks of second subject :"))
    sub3= int(input("Enter marks of third subject :"))
    sub4= int(input("Enter marks of fourth subject :"))
    sub5= int(input("Enter marks of fifth subject :"))

    total = sub1 + sub2 + sub3 + sub4 + sub5
    per = (total/500)*100

    if per>=90 and per<=100:
        return "Grade A+"
    elif per>=80 and per<90:
        return "Grade A"
    elif per>=70 and per<80:
        return "Grade B+"
    elif per>=60 and per<70:
        return "Grade B"
    elif per>=50 and per<60:
        return "Grade C"
    elif per>40 and per<90:
        return "Grade D"
    else:
        return "Fail"

Result = checkGrades()
print("Result of the student is :", Result)
print("-------------------------------------------------------------------------------------------")
#WITH PARAMETER WITHout RETURN TYPE
def checkGrades(sub1, sub2, sub3, sub4, sub5):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    per = (total/500)*100

    if per>=90 and per<=100:
        print("Grade A+")
    elif per>=80 and per<90:
        print("Grade A")
    elif per>=70 and per<80:
        print("Grade B+")
    elif per>=60 and per<70:
        print("Grade B")
    elif per>=50 and per<60:
        print("Grade C")
    elif per>40 and per<90:
        print("Grade D")
    else:
        print("Fail")

checkGrades(56,78,99,76,65)
print("-------------------------------------------------------------------------------------------")
#WITH PARAMETER WITH RETURN TYPE
def checkGrades(sub1, sub2, sub3, sub4, sub5):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    per = (total/500)*100
    if per>=90 and per<=100:
        return "Grade A+"
    elif per>=80 and per<90:
        return "Grade A"
    elif per>=70 and per<80:
        return "Grade B+"
    elif per>=60 and per<70:
        return "Grade B"
    elif per>=50 and per<60:
        return "Grade C"
    elif per>40 and per<90:
        return "Grade D"
    else:
        return "Fail"

Result = checkGrades()
print("Result of the student is :", Result)
print("-------------------------------------------------------------------------------------------")