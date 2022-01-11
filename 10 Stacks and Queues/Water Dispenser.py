from collections import deque

quantity = int(input())
names = deque()

command = input()

while True:
    if command == 'Start' or command == 'End':
        break
    else:
        names.append(command)

    command = input()

while True:
    command = input()
    if command == 'End':
        break
    c = command.split()
    if len(c) == 2:
        quantity += int(c[1])
    elif command == 'Start':
        continue
    else:
        if quantity - int(c[0]) >= 0:
            print(f"{names.popleft()} got water")
            quantity -= int(c[0])
        else:
            print(f"{names.popleft()} must wait")

print(f"{quantity} liters left")