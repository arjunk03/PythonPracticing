from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_type(self):
        pass
    
    @abstractmethod
    def get_specs(self):
        pass

# Concrete Vehicle classes
class Car(Vehicle):
    def __init__(self, model, engine_type, seats):
        self.model = model
        self.engine_type = engine_type
        self.seats = seats
        
    def get_type(self):
        return "Car"
    
    def get_specs(self):
        return f"{self.model} - {self.engine_type} engine, {self.seats} seats"

class Motorcycle(Vehicle):
    def __init__(self, model, engine_cc, has_sidecar):
        self.model = model
        self.engine_cc = engine_cc
        self.has_sidecar = has_sidecar
        
    def get_type(self):
        return "Motorcycle"
    
    def get_specs(self):
        sidecar = "with" if self.has_sidecar else "without"
        return f"{self.model} - {self.engine_cc}cc, {sidecar} sidecar"

class Truck(Vehicle):
    def __init__(self, model, cargo_capacity, wheels):
        self.model = model
        self.cargo_capacity = cargo_capacity
        self.wheels = wheels
        
    def get_type(self):
        return "Truck"
    
    def get_specs(self):
        return f"{self.model} - {self.cargo_capacity} tons capacity, {self.wheels} wheels"

# Vehicle Factory
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, *args):
        vehicles = {
            "car": Car,
            "motorcycle": Motorcycle,
            "truck": Truck
        }
        
        vehicle_class = vehicles.get(vehicle_type.lower())
        if not vehicle_class:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
            
        return vehicle_class(*args)

# Example usage
def main():
    factory = VehicleFactory()
    
    # Create different vehicles
    tesla = factory.create_vehicle("car", "Tesla Model 3", "Electric", 5)
    harley = factory.create_vehicle("motorcycle", "Harley Davidson", 1450, False)
    volvo = factory.create_vehicle("truck", "Volvo FH16", 40, 18)
    
    # Display vehicle information
    vehicles = [tesla, harley, volvo]
    
    print("Vehicle Factory Demo:")
    print("-" * 50)
    
    for vehicle in vehicles:
        print(f"Type: {vehicle.get_type()}")
        print(f"Specifications: {vehicle.get_specs()}")
        print("-" * 50)

if __name__ == "__main__":
    main()
