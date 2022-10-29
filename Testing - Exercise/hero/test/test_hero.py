import binhex
import unittest

from unittest import TestCase

from project.hero import Hero


class HeroTests(TestCase):
    username = 'Pavel'
    health = 100
    damage = 60
    level = 10

    def setUp(self) -> None:
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertEqual(self.level, self.hero.level)

    def test_type_of_init_attributes(self):
        self.hero.health = 100.0
        self.hero.damage = 60.1
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_battle__when_enemy_hero_username_is_same__expect_raise(self):
        hero = Hero(self.username, 12, 80, 60)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(hero)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle__when_health_less_or_equal_to_0__expect_raise(self):
        self.hero.health = 0
        hero = Hero('Pesho', 12, 80, 60)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle__when_enemy_hero_health_less_or_equal_to_0__expect_raise(self):
        hero = Hero('Pesho', 12, 0, 60)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(hero)

        self.assertEqual(f"You cannot fight {hero.username}. He needs to rest", str(ve.exception))

    def test_battle__expect_return_draw(self):
        hero = Hero('Pesho', 10, 100, 60)
        expected_info = 'Draw'
        actual_info = self.hero.battle(hero)

        self.assertEqual(expected_info, actual_info)

    def test_battle__when_enemy_hero_health_less_or_equal_to_0__expect_message(self):
        hero = Hero('Pesho', 1, 80, 40)
        expected_info = 'You win'
        actual_info = self.hero.battle(hero)

        self.assertEqual(expected_info, actual_info)
        self.assertEqual(self.level + 1, self.hero.level)
        self.assertEqual(65, self.hero.health)
        self.assertEqual(self.damage + 5, self.hero.damage)

    def test_battle__when_health_less_or_equal_to_0__expect_message(self):
        hero = Hero('Pesho', 10, 80, 40)
        self.hero.level = 2
        self.hero.damage = 30
        expected_info = 'You lose'
        actual_info = self.hero.battle(hero)

        self.assertEqual(expected_info, actual_info)
        self.assertEqual(11, hero.level)
        self.assertEqual(25, hero.health)
        self.assertEqual(45, hero.damage)

    def test_str_method(self):
        expected_info = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        actual_info = str(self.hero)

        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()