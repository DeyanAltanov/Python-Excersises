word = input()

characters = []

for character in word:
    characters.append(character)

strength = 0
index = 0

while index < len(characters):
    if characters[index] == '>' and characters[index + 1].isalnum():
        if characters[index + 1].isdigit():
            strength += int(characters[index + 1])
        if strength > 0:
            characters.pop(index + 1)
            strength -= 1
            index -= 1
    index += 1

print(''.join(characters))