command = input()
todo_list = [0] * 10

while not command == 'End':
    cmd = command.split('-')
    todo_list.insert(int(cmd[0]), cmd[1])
    command = input()

result = []

for i in todo_list:
    if i != 0:
        result.append(i)

print(result)