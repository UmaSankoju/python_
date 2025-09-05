
class Vehicle:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Vehicle:", self.name)


class Car(Vehicle):  # Single inheritance
    def drive(self):
        print(self.name, "is driving.")



class Electric:
    def charge(self):
        print("Charging the battery...")

class ElectricCar(Car, Electric):  # Multiple inheritance
    def drive(self):
        print(self.name, "is using power.")


class SportsCar(Car):  # Child of Car
    def turbo(self):
        print(self.name, "is in turbo mode!")


class RacingCar(SportsCar):  # Child of SportsCar
    def race(self):
        print(self.name, "is racing on the track!")


class Bike(Vehicle):   # Another child of Vehicle
    def ride(self):
        print(self.name, "is riding on two wheels.")


class HybridCar(Electric, Car):  # Inherits from both
    def eco_mode(self):
        print(self.name, "is running in eco mode.")


print("\nSingle Inheritance")
car = Car("Sedan")
car.show()
car.drive()

print("\nMultiple Inheritance ")
ev = ElectricCar("Tesla")
ev.show()
ev.drive()
ev.charge()

print("\nMultilevel Inheritance")
race = RacingCar("Ferrari")
race.show()
race.drive()
race.turbo()
race.race()

print("\n Hierarchical Inheritance ")
bike = Bike("Yamaha")
bike.show()
bike.ride()

print("\n Hybrid Inheritance")
hybrid = HybridCar("Prius")
hybrid.show()
hybrid.charge()
hybrid.eco_mode()
