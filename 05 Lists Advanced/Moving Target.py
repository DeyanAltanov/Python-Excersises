targets = [int(el) for el in input().split()]

cmd = [el for el in input().split()]
command = cmd[0]

while not command == 'End':
    index = int(cmd[1])
    value = int(cmd[2])

    if command == 'Shoot':
        if 0 <= index <= len(targets) - 1:
            if targets[index] - value <= 0:
                targets.pop(index)
            else:
                targets[index] -= value
    elif command == 'Add':
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        if 0 <= index <= len(targets) - 1 and index + value <= len(targets) - 1 and 0 <= index - value:
            del targets[index - value:(index + value) + 1]
        else:
            print('Strike missed!')
    cmd = [el for el in input().split()]
    command = cmd[0]

string_targets = [str(el) for el in targets]
print('|'.join(string_targets))