class Garage:
    vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)


class Vehicle:
    def __init__(self, make, age, model, engine):
        self.make = make
        self.age = age
        self.model = model
        self.engine = engine

    def __str__(self):
        return str(self.make)


class Car(Vehicle):
    def __init__(self, make, age, model, engine, door, windows):
        Vehicle.__init__(self, make, age, model, engine)
        self.windows = windows
        self.door = door
    pass


class Motocycle(Vehicle):
    pass


newcar1 = Car("toyota", 4, "corolla", "petrol", 5, 5)
newcar2 = Car("honda", 3, "civic", "diesel", 3, 5)
newcar3 = Car("tesla", 2, "model x", "electric", 5, 5)
newmoto1 = Motocycle("suzuki", 7, "A2", "petrol")
garage = Garage()
garage.add_vehicle(newcar1)
garage.add_vehicle(newcar1)
v1 = Motocycle("suzuki", 2, "500", "petrol")  #moto
print(garage.print_vehicles())
for vehicle in garage.vehicles:
    print(vehicle.make, vehicle.model, vehicle.age, vehicle.engine)
