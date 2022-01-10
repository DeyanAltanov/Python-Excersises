n = input().split(', ')

numbers = [int(el) for el in n]

evens = []

for number in range(0, len(numbers)):
    if numbers[number] % 2 == 0:
        evens.append(number)

print(evens)