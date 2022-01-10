numbers = input()

beggars_number = int(input())

all_beggars = numbers.split(', ')

beggars = [all_beggars[i:i + beggars_number] for i in range(0, len(all_beggars), beggars_number)]

home = [int(0)] * beggars_number

for i in beggars:
    for j in range(0, len(i)):
        home[j] += int(i[j])

print(home)