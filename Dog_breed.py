class Dog:
    # Class Variable
    animal = "Dog"

    # Constructor with Instance Variables
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    # Method to display details
    def display(self):
        print("Animal :", Dog.animal)
        print("Breed  :", self.breed)
        print("Colour :", self.colour)
        print()


# Creating two objects of different dog breeds
dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Labrador", "Golden")

# Display details
print("Dog 1 Details")
dog1.display()

print("Dog 2 Details")
dog2.display()