#ride calculator
distance = float(input("Enter the distance you want to travel:"))
base_fare = 20
if distance>0 and distance <=1:
    ride_charge = base_fare
    print("Your total charge is:", ride_charge, "Rupees")
elif distance>1 and distance<=5:
    ride_charge = base_fare + 6*distance
    print("Your total charge is:", ride_charge, "Rupees")
elif distance>5 and distance <=12:
    ride_charge = base_fare + 5.5*distance
    print("Your total charge is:", ride_charge , "Rupees")
elif distance>12 and distance<=20:
    ride_charge = base_fare + 5*distance
    print("Your total charge is:", ride_charge, "Rupees")
else:
    print("Sorry you have entered invalid distance.")
    print("Please try again & enter distance from 0 - 20 (in kms)")
