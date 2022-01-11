import re

regex_name = r"\%[A-Z][a-z]+\%"
regex_product = r"\<\w+\>"
regex_count = r"\|[0-9]+\|"
regex_price = r"\|([\w]+)?[0-9]+[\.]?[0-9]?\$"

order = input()
real_price = []
total_income = 0

while order != 'end of shift':
    name = re.findall(regex_name, order)
    product = re.findall(regex_product, order)
    count = re.findall(regex_count, order)
    price_info = re.finditer(regex_price, order)
    if name and product and count and price_info:
        n = name[0].replace('%', '')
        p = product[0].replace('<', '')
        p = p.replace('>', '')
        c = int(count[0].replace('|', ''))
        for char in price_info:
            real_price.append(char.group(0))
        if len(real_price) == 0:
            order = input()
            continue
        else:
            price = real_price[0]
            true_price = ''
            for char in price:
                if 48 <= ord(char) <= 57 or ord(char) == 46:
                    true_price += char
            print(f"{n}: {p} - {c * float(true_price):.2f}")
            total_income += c * float(true_price)
            real_price.pop(0)

    order = input()

print(f"Total income: {total_income:.2f}")