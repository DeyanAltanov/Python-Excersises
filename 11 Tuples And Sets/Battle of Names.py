names_count = int(input())

odds = set()
evens = set()

for i in range(1, names_count + 1):
    name = input()
    total = 0
    for letter in name:
        char = ord(letter)
        total += char
    total /= i
    total = int(total)
    if total % 2 == 0:
        evens.add(total)
    else:
        odds.add(total)

sum_odds = sum(odds)
sum_evens = sum(evens)

if sum_evens == sum_odds:
    print(', '.join(map(lambda number: str(number), odds.union(evens))))
elif sum_odds > sum_evens:
    print(', '.join(map(lambda number: str(number), odds.difference(evens))))
else:
    print(', '.join(map(lambda number: str(number), odds.symmetric_difference(evens))))