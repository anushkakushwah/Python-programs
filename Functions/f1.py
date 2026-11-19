# #WITHOUT PARAMETER WITHOUT RETURNTYPE
def sum():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a+b
    print("Addition is:", c)

print("Program starts here.")
sum()
print("Program ends here.")
sum()

# #WITHOUT PARAMETER WITH RETURN TYPE
def sum():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a+b
    return c

print(sum())

#WITH\ PARAMETER WITHOUT RETURN TYPE
def sum(a,b):
    c = a+b
    print("Adddition is : ", c)

sum(10,20)
a= int(input("Entr 1st number :"))
b =int(input("Enter 2nd number :"))
sum(a,b)

#WITH PARAMETER WITH RETURN TYPE
def sum(a,b):
    return a+b

print(sum(10,20))

