import unittest

from unittest import TestCase

from project.mammal import Mammal


class MammalTests(TestCase):
    name = 'Pesho'
    type = 'Monotremes'
    sound = 'HhH'
    kingdom = 'animals'

    def setUp(self) -> None:
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_init(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)

    def test_make_sound(self):
        expected_info = f"{self.name} makes {self.sound}"
        actual_info = self.mammal.make_sound()

        self.assertEqual(expected_info, actual_info)

    def test_get_kingdom(self):
        expected_info = self.kingdom
        actual_info = self.mammal.get_kingdom()

        self.assertEqual(expected_info, actual_info)

    def test_info(self):
        expected_info = f"{self.name} is of type {self.type}"
        actual_info = self.mammal.info()

        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()