print("Select your ride: ")
print("1. Car")
print("2. Bike")

choice = int(input("Enter your choice: "))
if choice == 1:
    print("What type of car: ")
    print("1. Sedan\n")
    print("2. SUV\n")

    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You choosed sedan.")
    else: 
        print("You choosed SUV.")
    
elif choice == 2:
    print("Enter your choice: ")
    print("1. Scooty\n")
    print("2. Bike\n")

    choice3 = int(input("Enter your choice: "))
    
    if choice3 == 1:
        print("You choosed scooty.")
    
    else:
        print("You choosed bike.")
    
else:
    print("Wrong choice.")


