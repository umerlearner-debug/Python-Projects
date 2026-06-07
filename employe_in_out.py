class employee:
    def __init__(self):
        print("Employee created.")

    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making object.")
    obj = employee()
    print("Function end....")
    return obj

print("calling create_obj() function....")
obj  = create_obj()
print("Program end...")
