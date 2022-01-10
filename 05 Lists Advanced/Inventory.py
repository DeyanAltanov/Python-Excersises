items = input().split(', ')

command = input()

while not command == 'Craft!':
    cmd = command.split(' - ')
    if cmd[0] == 'Collect':
        if cmd[1] not in items:
            items.append(cmd[1])
    elif cmd[0] == 'Drop':
        if cmd[1] in items:
            items.remove(cmd[1])
    elif cmd[0] == 'Combine Items':
        old_new = cmd[1].split(':')
        old = old_new[0]
        new = old_new[1]
        if old in items:
            index = items.index(old)
            items.insert(index + 1, new)
    elif cmd[0] == 'Renew':
        if cmd[1] in items:
            items.remove(cmd[1])
            items.append(cmd[1])

    command = input()

print(', '.join(items))