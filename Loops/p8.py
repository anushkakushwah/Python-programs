balance = 0

choice = 0

while choice != 4:
    print("\nEnter")
    print("1. Check Balance")
    print("2. Withdraw Balance")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance is:", balance)

    elif choice == 2:
        withdraw = int(input("Enter the amount to withdraw: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Balance left after withdrawal:", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Total Balance after deposit:", balance)

    elif choice == 4:
        print("Thank you!")

    else:
        print("Invalid Choice!")