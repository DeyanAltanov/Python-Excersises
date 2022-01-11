word = input()

characters = {}

for char in word:
    if char != ' ':
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

for character in characters:
    print(f"{character} -> {characters[character]}")