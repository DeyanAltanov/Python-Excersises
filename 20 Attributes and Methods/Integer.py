import math


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(math.floor(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for char in range(len(value)):
            number += roman_values[value[char]]
            if value[char] == 'V' and value[char - 1] == 'I' and char - 1 >= 0:
                number -= 2
            if value[char] == 'X' and value[char - 1] == 'I' and char - 1 >= 0:
                number -= 2
        return cls(number)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"

    def add(self, integer):
        if isinstance(integer, Integer):
            return self.value + integer.value
        return "number should be an Integer instance"