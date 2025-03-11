class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

class PassengerCar(Car):
    def __init__(self, brand, model, year, color, passengers):
        super().__init__(brand, model, year, color, passengers)
        self.passengers = passengers

class Truck(Car):
    def __init__(self, brand, model, year, color, capacity):
        super().__init__(brand, model, year, color)
        self.capacity = capacity

class Pickup(PassengerCar, Truck):
    def __init__(self, brand, model, year, color, passengers, capacity):
        PassengerCar.__init__(self, brand, model, year, color, passengers)
        Truck.__init__(self, brand, model, year, color, capacity)

pickup = Pickup('Ford', 'F150', 2020, 'black', 5, 1000)
print(pickup.brand)
