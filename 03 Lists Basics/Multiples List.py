factor = int(input())

count = int(input())

multiples = []

multiplier = 0

for i in range(0, count):
    multiplier += factor
    if multiplier % factor == 0:
        multiples.append(multiplier)

print(multiples)