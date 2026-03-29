# Take input from  the user.
unit = int(input("Enter the the number of units you consumed: "))

# Check for unit less than 50.
if (unit < 50):
    amount = unit * 2.60
    surcharge = 25

# Check for units less than 100.
elif (unit <= 100):
    amount = 130 + ((unit - 50) * 3.25)
    surcharge = 35

# Check for units less than or equal to 200.
elif (unit <= 200):
    amount = 130 + 162.50 + ((unit - 100) * 5.26)
    surcharge = 45

else:
    amount = 130 + 162.50 + 526 + ((unit - 200) * 8.26)
    surcharge = 75

total = amount + surcharge
print("\n Electricity bill = %.2f" % total)
     


    