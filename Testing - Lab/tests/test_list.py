import unittest

from unittest import TestCase

# from classes.list import IntegerList


class ListTest(TestCase):
    def setUp(self) -> None:
        self.ll = IntegerList(1, 2, 3)

    def test_init__expect_correct_data(self):
        self.assertEqual([1, 2, 3], self.ll._IntegerList__data)

        ll = IntegerList()
        self.assertEqual([], ll._IntegerList__data)

    def test_add__when_element_not_int__expect_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.ll.add('1')

    def test_add__expect_returning_list(self):
        self.ll.add(5)

        self.assertEqual([1, 2, 3, 5], self.ll._IntegerList__data)

    def test_remove_index__when_index_out_of_range__expect_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.ll.remove_index(3)

    def test_remove_index__when_index_is_correct__expect_return_element(self):
        actual_element = self.ll.remove_index(0)
        expected_element = 1

        self.assertEqual(expected_element, actual_element)

    def test_get__when_index_out_of_range__expect_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.ll.get(3)

    def test_get__when_index_is_correct__expect_returning_element(self):
        expected_element = 1
        actual_element = self.ll.get(0)

        self.assertEqual(expected_element, actual_element)

    def test_insert__when_index_out_of_range__expect_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.ll.insert(3, 3)

    def test_insert__when_element_not_int__expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.ll.insert(2, 2.5)

    def test_insert__when_all_is_correct__expect_correct_data(self):
        self.ll.insert(2, 4)

        expected_data = [1, 2, 4, 3]
        actual_data = self.ll._IntegerList__data

        self.assertEqual(expected_data, actual_data)

    def test_get_biggest__expect_returning_element(self):
        expected_element = 3
        actual_element = self.ll.get_biggest()

        self.assertEqual(expected_element, actual_element)

    def test_get_index__expect_returning_index(self):
        expected_index = 1
        actual_index = self.ll.get_index(2)

        self.assertEqual(expected_index, actual_index)


if __name__ == '__main__':
    unittest.main()
