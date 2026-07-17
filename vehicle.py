class BMW:
    def fuel_type(self):
        print("BMW Fuel Type: Petrol")

    def max_speed(self):
        print("BMW Max Speed: 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Ferrari Fuel Type: Petrol")

    def max_speed(self):
        print("Ferrari Max Speed: 340 km/h")


car1 = BMW()
car2 = Ferrari()

for car in (car1, car2):
    car.fuel_type()
    car.max_speed()
    print()