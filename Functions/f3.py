#even odd check with 4 types of functions
#WITHOUT PARAMETER WITHOUT RETURN TYPE
def checkEvenOdd():
    a = int(input("Enter a num :"))
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number")

checkEvenOdd()

#WITHOUT PARAMETER, WITH RETURN TYPE
def checkEvenOdd():
    a = int(input("Enter a num :"))
    if a%2 ==0:
        return ("Even Number.")
    else:
        return ("Odd Number.")

print(checkEvenOdd())

#WITH PARAMETER, WITHOUT RETURN TYPE
def checkEvenOdd(a):
    if a%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

checkEvenOdd(56)

#WITH PARAMETER, WITH RETURN TYPE
def checkEvenOdd(a):
    if a%2 == 0:
        return "Even Number"
    else:
        return "Odd number"
print(checkEvenOdd(769))

