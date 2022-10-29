import unittest
from unittest import TestCase

# from classes.cat import Cat


class CatTest(TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Pesho')

    def test_eat__expect_cat_size_to_be_increase(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test_eat__when_fed_is_false__expect_fed_to_be_true(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_eat__when_is_fed__expect_raise_error(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertIsNotNone(ex)

    def test_sleep__when_is_not_fed__expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)

    def test_sleep__when_is_fed__expect_sleep_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
