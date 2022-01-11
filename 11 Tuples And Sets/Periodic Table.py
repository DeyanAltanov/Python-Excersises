elements_count = int(input())

elements = set()

for _ in range(elements_count):
    compounds = input().split()
    for compound in compounds:
        elements.add(compound)

for element in elements:
    print(element)