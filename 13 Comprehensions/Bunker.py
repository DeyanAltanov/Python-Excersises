items = {item: {} for item in input().split(', ')}

n = int(input())
count_items = 0
total_quality = 0

for index in range(n):
    info = input().split(' - ')
    quantity_and_quality = info[2].split(';')
    quantity_and_value = quantity_and_quality[0].split(':')
    quality_and_value = quantity_and_quality[1].split(':')
    items[info[0]].update({info[1]: {quantity_and_value[0]: int(quantity_and_value[1]), quality_and_value[0]: int(quality_and_value[1])}})
    count_items += int(quantity_and_value[1])
    total_quality += int(quality_and_value[1])

print(f"Count of items: {count_items}")
print(f"Average quality: {total_quality / len(items):.2f}")

for item in items:
    print(f"{item} -> {', '.join(items[item])}")