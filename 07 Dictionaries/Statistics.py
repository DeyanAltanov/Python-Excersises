command = input().split(": ")
statistics = {}

while not command[0] == 'statistics':
    key = command[0]
    quantity = int(command[1])

    if key in statistics:
        statistics[key] += quantity
    else:
        statistics[key] = quantity

    command = input().split(": ")

total_quantity = 0

print("Products in stock:")
for product in statistics:
    print(f"- {product}: {statistics[product]}")
    total_quantity += statistics[product]

print(f"Total Products: {len(statistics)}")
print(f"Total Quantity: {total_quantity}")