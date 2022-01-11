from wild_farm.animals.animal import Mammal
from wild_farm.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"Mouse does not eat {food.__class__.__name__}!"
        self.gain_weight(0.10, food)


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Dog does not eat {food.__class__.__name__}!"
        self.gain_weight(0.40, food)


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if not isinstance(food, Meat) and not isinstance(food, Vegetable):
            return f"Cat does not eat {food.__class__.__name__}!"
        self.gain_weight(0.30, food)


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"Tiger does not eat {food.__class__.__name__}!"
        self.gain_weight(1.00, food)