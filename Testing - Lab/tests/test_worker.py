import unittest

from unittest import TestCase

from classes.worker import Worker


class WorkerTests(TestCase):
    NAME = "Pavel"
    SALARY = 3500
    ENERGY = 2

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_init__when_valid_props__expect_worker_with_correct_data(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest__expect_energy_increment(self):
        self.worker.rest()

        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test_work__when_energy_is_0__expect_raise_error(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertIsNotNone(ex)

    def test_work__when_enough_energy__expect_money_to_be_increase(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test_work__when_enough_energy__expect_energy_to_be_decrease(self):
        self.worker.work()

        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_get__info__expect_correct_result(self):
        expected = f'{self.NAME} has saved {0} money.'
        actual = self.worker.get_info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
