file = input().split("\\")

filename = file[-1]
characters = []
extension = []

for char in filename:
    characters.append(char)

for char in range(len(characters) - 1, 0, -1):
    if characters[char] == ".":
        characters.pop(char)
        break
    else:
        extension.append(characters.pop(char))

print(f"File name: {''.join(characters)}")
print(f"File extension: {''.join(reversed(extension))}")