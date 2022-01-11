from car_manager import Car
import unittest


class TestCar(unittest.TestCase):
    def test_valid__init__(self):
        car = Car('Audi', 'Q7', 10, 100)
        self.assertEqual('Audi', car.make)
        self.assertEqual('Q7', car.model)
        self.assertEqual(10, car.fuel_consumption)
        self.assertEqual(100, car.fuel_capacity)

    def test_invalid_make(self):
        car = Car('Audi', 'Q7', 10, 100)
        with self.assertRaises(Exception):
            car.make = ''

    def test_valid_make(self):
        car = Car('Audi', 'Q7', 10, 100)
        car.make = 'Mercedes'
        self.assertEqual('Mercedes', car.make)

    def test_invalid_model(self):
        car = Car('Audi', 'Q7', 10, 100)
        with self.assertRaises(Exception):
            car.model = ''

    def test_valid_model(self):
        car = Car('Audi', 'Q7', 10, 100)
        car.model = 'A6'
        self.assertEqual('A6', car.model)

    def test_invalid_fuel_consumption(self):
        car = Car('Audi', 'Q7', 10, 100)
        with self.assertRaises(Exception):
            car.fuel_consumption = 0

    def test_valid_fuel_consumption(self):
        car = Car('Audi', 'Q7', 10, 100)
        car.fuel_consumption = 8
        self.assertEqual(8, car.fuel_consumption)

    def test_invalid_fuel_capacity(self):
        car = Car('Audi', 'Q7', 10, 100)
        with self.assertRaises(Exception):
            car.fuel_capacity = 0

    def test_valid_fuel_capacity(self):
        car = Car('Audi', 'Q7', 10, 100)
        car.fuel_capacity = 200
        self.assertEqual(200, car.fuel_capacity)

    def test_invalid_fuel_amount(self):
        car = Car('Audi', 'Q7', 10, 100)
        with self.assertRaises(Exception):
            car.fuel_amount = -1

    def test_valid_fuel_amount(self):
        car = Car('Audi', 'Q7', 10, 100)
        car.fuel_amount = 300
        self.assertEqual(300, car.fuel_amount)

    def test_invalid_refuel(self):
        car = Car('Audi', 'Q7', 10, 100)
        with self.assertRaises(Exception):
            car.refuel(-1)

    def test_valid_refuel(self):
        car = Car('Audi', 'Q7', 10, 100)
        car.refuel(150)
        self.assertEqual(100, car.fuel_amount)

    def test_invalid_drive(self):
        car = Car('Audi', 'Q7', 10, 100)
        with self.assertRaises(Exception):
            car.drive(1000)

    def test_valid_drive(self):
        car = Car('Audi', 'Q7', 10, 100)
        car.fuel_amount = 100
        car.drive(1000)
        self.assertEqual(0, car.fuel_amount)


if __name__ == '__main__':
    unittest.main()