class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = float(length)
        self.single = bool(single)

    def get_info(self):
        return f"{self.name} - {self.length}"