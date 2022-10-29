import unittest

from unittest import TestCase

from project.student import Student


class StudentTests(TestCase):
    name = 'Pavel'
    courses = {'python advanced': ['note 1']}

    def setUp(self) -> None:
        self.student = Student(self.name, self.courses)

    def test_init(self):
        self.assertEqual(self.name, self.student.name)
        self.assertEqual(self.courses, self.student.courses)

        student = Student('Pesho')
        self.assertEqual("Pesho", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll__when_course_name_in_courses__expect_correct_message(self):
        actual_message = self.student.enroll('python advanced', ['note 2'])
        expected_message = "Course already added. Notes have been updated."

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(['note 1', 'note 2'], self.student.courses['python advanced'])

    def test_enroll__when_add_course_notes_is_empty__expect_correct_message(self):
        actual_message = self.student.enroll('python basics', ['note 1'])
        expected_message = "Course and course notes have been added."

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(['note 1'], self.student.courses['python basics'])
        self.assertTrue('python basics' in self.student.courses)

        actual_message = self.student.enroll('python', ['note 1'], 'Y')
        expected_message = "Course and course notes have been added."

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(['note 1'], self.student.courses['python basics'])
        self.assertTrue('python basics' in self.student.courses)

    def test_enroll__expect_correct_message(self):
        actual_message = self.student.enroll('python web', ['note 1'], 'A')
        expected_message = "Course has been added."

        self.assertEqual(expected_message, actual_message)
        self.assertEqual([], self.student.courses['python web'])
        self.assertTrue('python web' in self.student.courses)

    def test_add_notes__when_course_name_in_courses__expect_correct_message(self):
        actual_message = self.student.add_notes('python advanced', 'note 2')
        expected_message = "Notes have been updated"

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(['note 1', 'note 2'], self.student.courses['python advanced'])

    def test_add_notes__when_course_name_not_in_courses__expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('python web', ['october'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course__when_course_in_courses__expect_correct_message(self):
        actual_message = self.student.leave_course('python advanced')
        expected_message = "Course has been removed"

        self.assertEqual(expected_message, actual_message)
        self.assertEqual(self.courses, self.student.courses)
        self.assertFalse('python advanced' in self.student.courses)

    def test_leave_course__when_course_not_in_courses__expect_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('programing basic with C#')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    unittest.main()