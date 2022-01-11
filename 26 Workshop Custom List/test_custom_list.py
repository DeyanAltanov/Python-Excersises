from unittest import TestCase

from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.array = CustomList()

    def test_append_empty(self):
        self.array.append(1)
        values = list(self.array)
        self.assertEqual([1], values)

    def test_append_not_empty(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        values = list(self.array)
        self.assertEqual([1, 2, 3], values)

    def test_append_return_list(self):
        result = self.array.append(1)
        self.assertEqual(self.array, result)

    def test_append_1024_values(self):
        values = [x for x in range(1024)]
        [self.array.append(x) for x in values]
        list_values = list(self.array)
        self.assertEqual(values, list_values)

    def test_remove_valid_index(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        result = self.array.remove(2)
        self.assertEqual([1, 2, 4], list(self.array))
        self.assertEqual(3, result)

    def test_remove_invalid_index(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        with self.assertRaises(IndexError):
            self.array.remove(4)

    def test_get_valid_index(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        result = self.array.get(2)
        self.assertEqual(3, result)

    def test_get_invalid_index(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        with self.assertRaises(IndexError):
            self.array.get(4)

    def test_extend(self):
        self.array.append(1)
        self.array.extend([])
        self.assertListEqual([1], list(self.array))

    def test_extend_list(self):
        self.array.append(1)
        self.array.extend([2])
        self.assertListEqual([1, 2], list(self.array))

    def test_extend_generator(self):
        self.array.append(1)
        self.array.extend([x for x in range(1)])
        self.assertListEqual([1, 0], list(self.array))

    def test_extend_not_iterable(self):
        self.array.append(1)
        with self.assertRaises(ValueError):
            self.array.extend(2)

    def test_insert_valid_index(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.insert(2, 33)
        self.assertEqual([1, 2, 33, 3], list(self.array))

    def test_insert_invalid_index(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        with self.assertRaises(IndexError):
            self.array.insert(self.array.size() + 1, 2)

    def test_pop(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        result = self.array.pop()
        self.assertEqual(4, result)
        self.assertListEqual([1, 2, 3], list(self.array))

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.array.pop()

    def test_clear(self):
        [self.array.append(x) for x in range(15)]
        self.array.clear()
        self.assertEqual([], list(self.array))

    def test_index(self):
        [self.array.append(x) for x in range(15)]
        index = self.array.index(5)
        self.assertEqual(5, index)

    def test_index_missing(self):
        [self.array.append(x) for x in range(15)]
        with self.assertRaises(ValueError):
            self.array.index(17)

    def test_count(self):
        [self.array.append(x) for x in range(15)]
        result = 1
        actual = self.array.count(5)
        self.assertEqual(result, actual)

    def test_count_multiple_times(self):
        [self.array.append(x) for x in range(15)]
        self.array.append(5)
        self.array.insert(3, 5)
        self.array.insert(7, 5)
        self.array.insert(1, 5)
        self.array.insert(9, 5)
        expected = 6
        actual = self.array.count(5)
        self.assertEqual(expected, actual)

    def test_count_missing(self):
        [self.array.append(x) for x in range(15)]
        expected = 0
        actual = self.array.count(55)
        self.assertEqual(expected, actual)

    def test_reverse(self):
        [self.array.append(x) for x in range(5)]
        expected = [x for x in range(4, -1, -1)]
        actual = self.array.reverse()
        self.assertEqual(expected, actual)

    def test_copy(self):
        [self.array.append(x) for x in range(5)]
        copied = self.array.copy()
        expected = [x for x in range(5)]
        actual = list(copied)
        self.assertNotEqual(copied, self.array)
        self.assertEqual(expected, actual)

    def test_add_first(self):
        self.array.add_first(1)
        self.assertEqual([1], list(self.array))

    def test_add_first_not_empty(self):
        [self.array.append(x) for x in range(5)]
        self.array.add_first(1)
        self.assertListEqual([1, 0, 1, 2, 3, 4], list(self.array))

    def test_dictionize_empty(self):
        actual = self.array.dictionize()
        expected = {}
        self.assertDictEqual(expected, actual)

    def test_dictionize_even(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        actual = self.array.dictionize()
        expected = {1: 2, 3: 4}
        self.assertDictEqual(expected, actual)

    def test_dictionize_odd(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        actual = self.array.dictionize()
        expected = {1: 2, 3: ' '}
        self.assertDictEqual(expected, actual)

    def test_move(self):
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.move(1)
        self.assertListEqual([2, 3, 1], list(self.array))

    def test_overbound(self):
        values = [x for x in range(15)]
        [self.array.append(x) for x in values]
        expected = max(values)
        actual = self.array.overbound()
        self.assertEqual(expected, actual)

    def test_underbound(self):
        values = [x for x in range(15)]
        [self.array.append(x) for x in values]
        expected = min(values)
        actual = self.array.underbound()
        self.assertEqual(expected, actual)

    def test_sum(self):
        self.array.append(1)
        self.array.append('2')
        self.array.append(3)
        expected = 5
        actual = self.array.sum()
        self.assertEqual(expected, actual)

    def test_sum_empty(self):
        self.assertEqual(0, self.array.sum())