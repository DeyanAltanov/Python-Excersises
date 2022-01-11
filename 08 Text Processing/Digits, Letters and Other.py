n = input()

digits = ''
letters = ''
signs = ''

for i in range(0, len(n)):
    if n[i].isnumeric():
        digits += n[i]
    elif n[i].isalpha():
        letters += n[i]
    else:
        signs += n[i]

print(digits)
print(letters)
print(signs)