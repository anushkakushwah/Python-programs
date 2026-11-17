#to check if password is valid or not
password= input("Enter password:")
capital = False 
small = False
Digit = False
special = False
if len(password)>= 8:
    for ch in password:
       if ch. isupper():
           capital = True
       elif  ch. islower():
           small = True
       elif ch. isdigit():
          digit = True
       else :
            special = True
    if capital and small and digit and special:
        print("Valid Password.")
    else:
        print("Invalid  password")
        print("\n Your password should contain:")
        print("\n Atleast 8 Characters.")
        print("\n Atleast One Upper char...")
        print("\n Atleast One lower char...")
        print("\n Atleast One Digit...")
        print("\n Atleast One Special Character...!")
           
else:
    print("password must be contain at least 8 characters !!")