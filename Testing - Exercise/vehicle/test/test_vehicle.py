import unittest

from unittest import TestCase

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    fuel = 50
    horse_power = 150
    fuel_consumption = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_type_of_class_attributes(self):
        vehicle = Vehicle(55.5, 150.5)
        self.assertIsInstance(vehicle.fuel, float)
        self.assertIsInstance(vehicle.horse_power, float)

    def test_drive__when_fuel_not_enough__expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive__when_fuel_is_enough__expect_correct_result(self):
        self.vehicle.drive(30)
        expected_info = 12.5
        actual_info = self.vehicle.fuel

        self.assertEqual(expected_info, actual_info)

    def test_refuel__when_capacity_not_enough__expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)

        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel__when_capacity_is_enough__expect_correct_result(self):
        self.vehicle.drive(30)
        self.vehicle.refuel(30)
        expected_info = 42.5
        actual_info = self.vehicle.fuel

        self.assertEqual(expected_info, actual_info)

    def test_str_method(self):
        expected_result = f"The vehicle has {self.horse_power} " \
                          f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
        actual_result = self.vehicle.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
