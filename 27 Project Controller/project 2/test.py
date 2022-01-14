from unittest import TestCase, main
from project_2.movie import Movie


class TestHardware(TestCase):
    def setUp(self):
        self.movie = Movie("Serbian Film", 2010, 10)

    def test_attributes(self):
        self.assertEqual("Serbian Film", self.movie.name)
        self.assertEqual(2010, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_invalid_year(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_append_actor(self):
        self.movie.actors.append("Andela Nenadovic")
        self.assertEqual(1, len(self.movie.actors))

    def test_gt_g(self):
        second_movie = Movie("Friday 13", 2010, 9)
        self.assertEqual('"Serbian Film" is better than "Friday 13"', self.movie.__gt__(second_movie))

    def test_gt_l(self):
        second_movie = Movie("Friday 13", 2010, 11)
        self.assertEqual('"Friday 13" is better than "Serbian Film"', self.movie.__gt__(second_movie))


if __name__ == 'main':
    main()