import re

all_participants = input().split(', ')

participants = {}

for participant in all_participants:
    participants[participant] = 0

command = input()

letters = r"[a-zA-Z]"
digits = r"[0-9]"

while command != 'end of race':
    name_letters = re.findall(letters, command)
    name = ''
    for char in name_letters:
        name += char
    if name in participants:
        all_digits = re.findall(digits, command)
        distance = 0
        for digit in range(len(all_digits)):
            distance += int(all_digits[digit])
        participants[name] += int(distance)

    command = input()

ordered_participants = sorted(participants.items(), key=lambda item: item[1], reverse=True)

print(f"1st place: {ordered_participants[0][0]}")
print(f"2nd place: {ordered_participants[1][0]}")
print(f"3rd place: {ordered_participants[2][0]}")