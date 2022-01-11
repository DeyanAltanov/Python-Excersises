from extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def test_add(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add('hui')

    def test_remove(self):
        integer_list = IntegerList()
        with self.assertRaises(IndexError):
            integer_list.remove_index(0)

    def test_valid__init__(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(3, len(integer_list.get_data()))

    def test_invalid__init__(self):
        integer_list = IntegerList(1, 2, 'hui')
        self.assertEqual(2, len(integer_list.get_data()))

    def test_get(self):
        integer_list = IntegerList()
        with self.assertRaises(IndexError):
            integer_list.get(1)

    def test_insert_out_of_range(self):
        integer_list = IntegerList(1)
        with self.assertRaises(IndexError):
            integer_list.insert(1, 2)

    def test_insert_not_int(self):
        integer_list = IntegerList(1)
        with self.assertRaises(ValueError):
            integer_list.insert(0, 'hui')

    def test_get_biggest(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(3, integer_list.get_biggest())

    def test_get_index(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(0, integer_list.get_index(1))


if __name__ == '__main__':
    unittest.main()