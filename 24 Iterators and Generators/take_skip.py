class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_step = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            current_step = self.current_step
            self.current_step += self.step
            self.counter += 1
            return current_step
        raise StopIteration()