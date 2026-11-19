#NAME AND  MARKS INPUT AND TELL IF THE STUDENT PASSED OR FAIL..
#even odd check with 4 types of functions
#WITHOUT PARAMETER WITHOUT RETURN TYPE
def checkPassFail():
    name = input("Enter your name : ")
    marksinper = int(input("Enter Marks in percentage :"))
    if marksinper>=33:
        print("Result is : Pass")
    else:
        print("Result is : Fail")

checkPassFail()

#WITHOUT PARAMETER, WITH RETURN TYPE
def checkPassFail():
    name = input("Enter your name : ")
    marksinper = int(input("Enter Marks in percentage :"))
    if marksinper>=33:
        return ("Result is : Pass.")
    else:
        return ("Result is : Fail.")
result = checkPassFail()
print("Result for student is :", result)

#WITH PARAMETER, WITHOUT RETURN TYPE
def checkPassFail(name, marksinper):
    if marksinper>=33:
        print("Result is : Pass")
    else:
        print("Result is : Fail")

checkPassFail("Arjit", 78)

#WITH PARAMETER, WITH RETURN TYPE
def checkPassFail(name,marksinper):
    if marksinper>=33:
        return "Result is : Pass"
    else:
        return "Result is : Fail"
print(checkPassFail("Akanksha", 45))

