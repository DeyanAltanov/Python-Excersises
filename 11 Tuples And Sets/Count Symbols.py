text = input()
characters = {}

for char in range(len(text)):
    if text[char] not in characters:
        characters[text[char]] = 1
    else:
        characters[text[char]] += 1

characters = dict(sorted(characters.items()))

for char, occurrences in characters.items():
    print(f"{char}: {occurrences} time/s")