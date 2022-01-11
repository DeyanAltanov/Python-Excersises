import re

text = input()

regex = "\\d+"
all_numbers = []

while text:
    numbers = re.findall(regex, text)
    if numbers:
        all_numbers.extend(numbers)
    text = input()

for number in all_numbers:
    print(number, end=' ')