all_numbers = tuple(input().split())

numbers = {}

for number in all_numbers:
    if float(number) not in numbers:
        numbers[float(number)] = 1
    else:
        numbers[float(number)] += 1

for number, occurrences in numbers.items():
    print(f"{number} - {occurrences} times")