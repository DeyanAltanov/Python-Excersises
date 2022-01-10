numbers = input()

numbers_list = numbers.split(' ')

numbers_opposite = [int(0)] * len(numbers_list)

for number in range(0, len(numbers_list)):
    numbers_opposite[number] -= int(numbers_list[number])

print(numbers_opposite)