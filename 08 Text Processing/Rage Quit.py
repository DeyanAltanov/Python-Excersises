text = input()

strings = ['']
repeats = []
unique_strings = []
index = 0
word = ''
value = ''

for char in range(0, len(text)):
    if text[char].isdigit():
        if value is True:
            value = False
            continue
        index += 1
        strings.append('')
        repeats.append(text[char])
        if char + 1 < len(text) and text[char + 1].isdigit():
            repeats[index - 1] += text[char + 1]
            value = True
    else:
        strings[index] += text[char].upper()

strings.pop()

for string in range(0, len(strings)):
    word += strings[string] * int(repeats[string])

print(f"Unique symbols used: {len(set(word))}")
print(word)