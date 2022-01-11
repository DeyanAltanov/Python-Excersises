command = input()

phonebook = {}

while True:
    if command.isdigit():
        break
    else:
        name_number = command.split('-')
        name = name_number[0]
        number = name_number[1]
        phonebook[name] = number
    command = input()

for _ in range(int(command)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")