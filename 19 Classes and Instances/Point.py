import math


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def set_x(self, new_x):
        self.x = int(new_x)

    def set_y(self, new_y):
        self.y = int(new_y)

    def distance(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)