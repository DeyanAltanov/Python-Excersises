text = input()

emoticons = []

for char in range(len(text)):
    if text[char] == ':':
        emoticons.append(text[char + 1])

for emoticon in emoticons:
    print(f":{emoticon}")