numbers = [int(el) for el in input().split(', ')]

last_element = max(numbers)

rounded_last = round(last_element, -1)

current_ten = 0

while current_ten <= rounded_last:
    group = [number for number in numbers if current_ten < number <= current_ten + 10]
    if current_ten == rounded_last:
        if len(group) == 0:
            break
    print(f"Group of {current_ten + 10}'s: {group}")
    current_ten += 10