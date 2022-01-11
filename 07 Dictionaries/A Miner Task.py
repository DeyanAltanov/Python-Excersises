resource = input()
resources = {}

while resource != 'stop':
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

    resource = input()

for resource in resources:
    print(f"{resource} -> {resources[resource]}")