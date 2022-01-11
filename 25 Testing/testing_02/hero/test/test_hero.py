from unittest import TestCase, main

from hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Main Hero", 10, 100, 10)
        self.enemy_hero = Hero("Enemy", 10, 100, 10)

    def test_check_attr_are_set(self):
        self.assertEqual("Main Hero", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_same_name(self):
        self.enemy_hero.username = "Main Hero"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hp_equal_to_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_hp_lower_than_zero(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_hp_equal_to_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_enemy_hp_lower_than_zero(self):
        self.enemy_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_draw_hp_equal_to_zero(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_draw_hp_less_than_zero(self):
        self.hero.level = 11
        self.enemy_hero.level = 11
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(-10, self.hero.health)
        self.assertEqual(-10, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_you_win_equal_to_zero(self):
        self.enemy_hero.level = 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_you_win_less_than_zero(self):
        self.hero.level = 11
        self.enemy_hero.level = 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(-10, self.enemy_hero.health)
        self.assertEqual(12, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_you_lose_equal_to_zero(self):
        self.hero.level = 4
        self.hero.health = 110
        self.enemy_hero.level = 11
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(12, self.enemy_hero.level)
        self.assertEqual(65, self.enemy_hero.health)
        self.assertEqual(15, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_battle_you_lose_less_than_zero(self):
        self.enemy_hero.level = 12
        self.hero.level = 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(-20, self.hero.health)
        self.assertEqual(13, self.enemy_hero.level)
        self.assertEqual(55, self.enemy_hero.health)
        self.assertEqual(15, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_repr(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\nHealth: {self.hero.health}\nDamage: {self.hero.damage}\n", str(self.hero))


if __name__ == '__main__':
    main()