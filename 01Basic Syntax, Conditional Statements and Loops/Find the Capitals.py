string = input()
list = []

for char in range(len(string)):
    letter = ord(string[char])
    if letter in range(65, 90):
        list.append(char)

print(list)