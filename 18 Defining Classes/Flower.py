class Flower:
    is_happy = False


    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = int(water_requirements)


    def water(self, water):
        if int(water) >= self.water_requirements:
            self.is_happy = True


    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"