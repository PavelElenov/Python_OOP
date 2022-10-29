from project.movie import Movie
import unittest
from unittest import TestCase


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('SpiderMan', 2021, 8.5)

    def test_init(self):
        self.assertEqual('SpiderMan', self.movie.name)
        self.assertEqual(2021, self.movie.year)
        self.assertEqual(8.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

        with self.assertRaises(ValueError) as ve:
            Movie('', 2021, 8.5)
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            Movie('Dune', 120, 8.5)
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor(self):
        self.movie.add_actor('Pavel Elenov')
        self.movie.add_actor('Petar Chernaev')
        self.assertEqual(['Pavel Elenov', 'Petar Chernaev'], self.movie.actors)
        result = self.movie.add_actor('Pavel Elenov')
        self.assertEqual("Pavel Elenov is already added in the list of actors!", result)

    def test_gt_method(self):
        other = Movie("SuperMan", 2020, 7.0)
        result = self.movie > other
        self.assertEqual('"SpiderMan" is better than "SuperMan"', result)

        other.rating = 9.0
        result = self.movie > other
        self.assertEqual('"SuperMan" is better than "SpiderMan"', result)

    def test_repr_method(self):
        self.movie.add_actor('Pavel')
        self.movie.add_actor('Petar')
        result = self.movie.__repr__()
        expected_result = f"Name: {self.movie.name}\n"\
                          f"Year of Release: {self.movie.year}\n" \
                          f"Rating: {self.movie.rating:.2f}\n" \
                          f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
