# Take input from student that he can attend the exam or not.
Medical_cause = input("Did you have a medical cause? (Y/N)").strip().upper()

# checking the user input and predicting output accordingly.
if Medical_cause == 'Y':
    print("You are allowed.")

else: 
    # Take input of attendance.
    attend = int(input("Enter the attendance percentage of the student: "))
    if attend >= 75:
        print("You are allowed.")

    else:
        print("Not allowed.")
