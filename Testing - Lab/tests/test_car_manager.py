import unittest

from unittest import TestCase

# from CarManager.car_manager import Car


class CarManagerTests(TestCase):
    def setUp(self) -> None:
        self.car = Car('Bulgaria', 'Mercedes', 50, 100)

    def test_init(self):
        self.assertEqual('Bulgaria', self.car.make)
        self.assertEqual('Mercedes', self.car.model)
        self.assertEqual(50, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter__when_make_is_invalid__expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

    def test_model_setter__when_model_is_invalid_expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

    def test_fuel_consumption_setter__when_is_invalid__expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -10

    def test_fuel_capacity_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

    def test_fuel_amount_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -100

    def test_refuel__when_fuel_is_invalid__expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

    def test_refuel__when_fuel_is_valid__expect_raise(self):
        self.car.refuel(50)

        expected_info = 50
        actual_info = self.car.fuel_amount
        self.assertEqual(expected_info, actual_info)

        self.car.refuel(110)
        expected_info = 100
        actual_info = self.car.fuel_amount
        self.assertEqual(expected_info, actual_info)

    def test_drive__when_dont_have_enough_fuel__expect_raise(self):
        self.car.fuel_amount = 20
        with self.assertRaises(Exception) as ex:
            self.car.drive(50)

    def test_drive__when_have_enough_fuel(self):
        self.car.fuel_amount = 20
        self.car.drive(30)
        expected_info = 5.0
        actual_info = self.car.fuel_amount
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
