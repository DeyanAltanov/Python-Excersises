substring = input()

word = input()

while True:
    if substring in word:
        word = word.replace(substring, '')
    else:
        break

print(word)