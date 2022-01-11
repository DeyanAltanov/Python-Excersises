class ReverseIter:
    def __init__(self, numbers):
        self.list = list(numbers)
        self.index = len(self.list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        index = self.list[self.index]
        self.index -= 1
        return index