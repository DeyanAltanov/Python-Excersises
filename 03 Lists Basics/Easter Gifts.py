all_gifts = input()
gifts = all_gifts.split(' ')

command = input()
cmd = []

while not command == 'No Money':
    cmd = command.split(' ')

    if cmd[0] == 'OutOfStock':
        for i in range(0, len(gifts)):
            if gifts[i] == cmd[1]:
                gifts[i] = 'None'
    elif cmd[0] == 'Required' and 0 <= int(cmd[2]) <= len(gifts) - 1:
        gifts[int(cmd[2])] = cmd[1]
    elif cmd[0] == 'JustInCase':
        gifts[-1] = cmd[1]

    command = input()

while 'None' in gifts:
    gifts.remove('None')

for gift in gifts:
    print(f"{gift} ", end='')