class Cup:
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)


    def fill(self, milliliters):
        if int(milliliters) <= self.size - self.quantity:
            self.quantity += milliliters


    def status(self):
        return self.size - self.quantity