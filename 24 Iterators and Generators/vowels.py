class Vowels:
    def __init__(self, word):
        self.word = word
        self.index = -1
        self.vowels = Vowels.all_vowels(self.word)

    @staticmethod
    def all_vowels(word):
        vowels = ''
        for char in word:
            if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'U' or char == 'u':
                vowels += char
        return vowels

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.vowels):
            raise StopIteration
        return self.vowels[self.index]