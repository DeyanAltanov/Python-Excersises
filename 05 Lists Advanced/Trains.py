wagons = [0] * int(input())

command = input()

while not command == 'End':
    cmd = command.split()
    if cmd[0] == 'add':
        last_wagon = len(wagons) - 1
        wagons[last_wagon] += int(cmd[1])
    elif cmd[0] == 'insert':
        wagons[int(cmd[1])] += int(cmd[2])
    elif cmd[0] == 'leave':
        if wagons[int(cmd[1])] - int(cmd[2]) < 0:
            wagons[int(cmd[1])] = 0
        else:
            wagons[int(cmd[1])] -= int(cmd[2])

    command = input()

print(wagons)