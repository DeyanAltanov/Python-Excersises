n = input()
m = int(input())


def order(product, quantity):
    result = None
    if product == 'coffee':
        result = quantity * 1.50
    elif product == 'water':
        result = quantity * 1.00
    elif product == 'coke':
        result = quantity * 1.40
    elif product == 'snacks':
        result = quantity * 2.00
    return result


print(f"{order(n, m):.2f}")