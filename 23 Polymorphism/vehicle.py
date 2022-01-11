from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        self.fuel_consumption += 0.9
        if self.fuel_consumption * distance <= self.fuel_quantity:
            self.fuel_quantity -= self.fuel_consumption * distance


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

    def drive(self, distance):
        self.fuel_consumption += 1.6
        if self.fuel_consumption * distance <= self.fuel_quantity:
            self.fuel_quantity -= self.fuel_consumption * distance