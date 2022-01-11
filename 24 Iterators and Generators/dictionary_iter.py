class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.current_index = 0
        self.items = list(self.dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.dictionary):
            index = self.current_index
            self.current_index += 1
            return self.items[index]
        raise StopIteration()