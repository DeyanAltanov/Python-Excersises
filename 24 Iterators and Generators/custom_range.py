class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration
        index = self.index
        self.index += 1
        return index