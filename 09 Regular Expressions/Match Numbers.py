import re

all_numbers = input()

matched_numbers = []

regex = "((^|(?<=\s))-?\d+(\.\d+)?($|(?=\s)))"

numbers = re.finditer(regex, all_numbers)

for number in numbers:
    matched_numbers.append(number.group(0))

for number in matched_numbers:
    print(number, end=' ')