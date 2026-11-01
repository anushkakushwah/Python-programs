## interest calculation
# balance 0-3k = 3%
#balance > 3k , ,<15k = 3%
#balance >15k <45k = 4%
#balance >45k <100k = 6%
#balance >100k = 7%
balance = float(input("Enter your balance:"))
if balance>=0 and balance<3000:
    interest = (0/100)*balance
    print("Interest on you will be 0%:", interest)
    total = balance + interest
    print("Total amount is:", total)
elif  balance>=3000 and balance<15000:
    interest = (3/100)*balance
    print("Interest on you will be 3%:", interest)
    total = balance + interest
    print("Total amount is:", total)
elif  balance>=15000 and balance<45000:
    interest = (4/100)*balance
    print("Interest on you will be 4%:", interest)
    total = balance + interest
    print("Total amount is:", total)
elif  balance>=45000 and balance<100000:
    interest = (6/100)*balance
    print("Interest on you will be 6%:", interest)
    total = balance + interest
    print("Total amount is:", total)
else:
    interest = (7/100)*balance
    print("Interest on you will be 7%:", interest)
    total = balance + interest
    print("Total amount is:", total)
    
    
