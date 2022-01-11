class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current = 0
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.number:
            self.current += 1
            if self.current_index < len(self.sequence):
                index = self.current_index
                self.current_index += 1
            else:
                self.current_index = 0
                index = self.current_index
                self.current_index += 1
            return self.sequence[index]
        raise StopIteration()