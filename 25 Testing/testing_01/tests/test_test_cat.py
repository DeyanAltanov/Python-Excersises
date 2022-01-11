from test_cat import Cat
import unittest


class TestCat(unittest.TestCase):
    name = 'Pussy'

    def setUp(self):
        self.cat = Cat(self.name)

    def test_size_eat(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_sleep(self):
        self.cat.fed = False
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_not_sleepy_while_fed(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()