from unittest import TestCase, main

from mammal.project.mammal import Mammal


class TestHero(TestCase):
    def setUp(self):
        self.mammal = Mammal("Pesho", "dog", "bark")

    def test_attr_set(self):
        self.assertEqual("Pesho", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("bark", self.mammal.sound)

    def test_make_sound(self):
        self.assertEqual("Pesho makes bark", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Pesho is of type dog", self.mammal.info())


if __name__ == '__main__':
    main()