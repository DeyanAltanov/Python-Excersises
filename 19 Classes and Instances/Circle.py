class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = int(radius)

    def set_radius(self, new_radius):
        self.radius = int(new_radius)

    def get_area(self):
        result = f"{(self.radius * self.radius) * Circle.pi:.2f}"
        return float(result)

    def get_circumference(self):
        return 2 * Circle.pi * self.radius