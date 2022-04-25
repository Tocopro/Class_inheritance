class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


school_bus = Bus("School Volvo", 180, 22)
print(school_bus.color, school_bus.name, " Speed:", school_bus.max_speed, " Mileage:", school_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, " Speed:", car.max_speed, " Mileage:", car.mileage)
