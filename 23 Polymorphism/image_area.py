class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, image):
        return self.get_area() > image.get_area()

    def __lt__(self, image):
        return self.get_area() < image.get_area()

    def __ge__(self, image):
        return self.get_area() >= image.get_area()

    def __le__(self, image):
        return self.get_area() <= image.get_area()

    def __eq__(self, image):
        return self.get_area() == image.get_area()

    def __ne__(self, image):
        return self.get_area() != image.get_area()