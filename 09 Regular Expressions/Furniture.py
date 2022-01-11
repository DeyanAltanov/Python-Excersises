import re

command = input()
all_furniture = []
bought_furniture = []
regex = r">>[a-zA-Z]+<<\d+\.?\d+!\d+\b"
spent = 0

while command != 'Purchase':
    elements = re.findall(regex, command)
    if len(elements) > 0:
        all_elements = re.finditer(regex, command)

        for f in all_elements:
            all_furniture.append(f.group(0))

        furniture_price_quantity = command.split('<<')
        furniture = furniture_price_quantity[0].split('>>')
        bought_furniture.append(furniture)
        price_quantity = furniture_price_quantity[1].split('!')
        price = float(price_quantity[0])
        quantity = int(price_quantity[1])
        spent += price * quantity

    command = input()

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture[1])
print(f"Total money spend: {spent:.2f}")