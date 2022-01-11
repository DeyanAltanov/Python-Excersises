word = input()

characters = [word[0]]

for char in range(0, len(word) - 1):
    if word[char] != word[char + 1]:
        characters.append(word[char + 1])

print(''.join(characters))