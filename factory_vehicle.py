class Vehicle:
    def manufacture(self):
        pass

class Car(Vehicle):
    def manufacture(self):
        return "Manufacturing Car"

class Motorcycle(Vehicle):
    def manufacture(self):
        return "Manufacturing Motorcycle"

class Truck(Vehicle):
    def manufacture(self):
        return "Manufacturing Truck"

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'motorcycle':
            return Motorcycle()
        elif vehicle_type == 'truck':
            return Truck()
        else:
            raise ValueError("Unknown Vehicle Type")

if __name__ == "__main__":
    factory = VehicleFactory()
    vehicle = factory.create_vehicle('motorcycle')
    print(vehicle.manufacture())
