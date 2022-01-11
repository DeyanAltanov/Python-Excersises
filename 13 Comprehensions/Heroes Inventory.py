names = {name: {'items': [], 'cost': 0} for name in input().split(', ')}

command = input().split('-')

while command[0] != 'End':
    name = command[0]
    item = command[1]
    cost = int(command[2])
    if item not in names[name]['items']:
        names[name]['items'].append(item)
        names[name]['cost'] += cost

    command = input().split('-')

print(*[f"{name} -> Items: {len(names[name]['items'])}, Cost: {names[name]['cost']}" for name in names], sep='\n')