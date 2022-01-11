text = input()

s = []

for char in text:
    s.append(char)

while s:
    print(s.pop(), end='')