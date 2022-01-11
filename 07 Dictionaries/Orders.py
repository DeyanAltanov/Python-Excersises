command = input()
products = {}

while command != 'buy':
    stuff = command.split()
    name = stuff[0]
    price = float(stuff[1])
    quantity = int(stuff[2])

    if name not in products:
        products[name] = []
        products[name].append(price)
        products[name].append(quantity)
    else:
        products[name][1] += quantity
        if price != products[name][0]:
            products[name][0] = price

    command = input()

for product in products:
    price = products[product][0] * products[product][1]
    print(f"{product} -> {price:.2f}")