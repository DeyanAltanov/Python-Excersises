numbers = [int(el) for el in input().split(', ')]
positives = [el for el in numbers if el >= 0]
negatives = [el for el in numbers if el < 0]
evens = [el for el in numbers if el % 2 == 0]
odds = [el for el in numbers if el % 2 == 1]

print("Positive: ", end='')
print(*positives, sep=', ')
print("Negative: ", end='')
print(*negatives, sep=', ')
print("Even: ", end='')
print(*evens, sep=', ')
print("Odd: ", end='')
print(*odds, sep=', ')