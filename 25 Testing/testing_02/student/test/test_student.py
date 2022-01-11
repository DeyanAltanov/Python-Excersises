from unittest import TestCase, main

from student.project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Student")

    def test_attr_set(self):
        self.assertEqual("Student", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)

    def test_enroll_with_notes(self):
        result = self.student_1.enroll("Python OOP", ['Solid', "Inheritance"])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_without_saving(self):
        result = self.student_1.enroll("Python OOP", ['Solid', "Inheritance"], "N")
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(0, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course has been added.", result)

    def test_enroll_course_exists(self):
        result = self.student_1.enroll("Python OOP", ['Solid', "Inheritance"])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)
        result = self.student_1.enroll("Python OOP", ['Abstraction', "Testing"])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(4, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_no_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("Python OOP", ["1", "2"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes(self):
        self.student_1.enroll("Python OOP", ['Solid', "Inheritance"])
        result = self.student_1.add_notes("Python OOP", "1")
        self.assertEqual(3, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Python OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.student_1.enroll("Python OOP", ['Solid', "Inheritance"])
        result = self.student_1.leave_course("Python OOP")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(0, len(self.student_1.courses))


if __name__ == '__main__':
    main()