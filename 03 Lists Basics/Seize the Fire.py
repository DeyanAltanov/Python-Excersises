all_cells = input()
water = int(input())
remaining_water = water
effort = 0.0
fires_seized = []

cells = all_cells.split('#')
cls = []

for cell in range(0, len(cells)):
    cls.append(cells[cell].split(' = '))
    if cls[cell][0] == 'Low':
        if 1 <= int(cls[cell][1]) <= 50:
            if remaining_water - int(cls[cell][1]) >= 0:
                remaining_water -= int(cls[cell][1])
                effort += 0.25 * int(cls[cell][1])
                fires_seized.append(cls[cell])
    elif cls[cell][0] == 'Medium':
        if 51 <= int(cls[cell][1]) <= 80:
            if remaining_water - int(cls[cell][1]) >= 0:
                remaining_water -= int(cls[cell][1])
                effort += 0.25 * int(cls[cell][1])
                fires_seized.append(cls[cell])
    elif cls[cell][0] == 'High':
        if 81 <= int(cls[cell][1]) <= 125:
            if remaining_water - int(cls[cell][1]) >= 0:
                remaining_water -= int(cls[cell][1])
                effort += 0.25 * int(cls[cell][1])
                fires_seized.append(cls[cell])

print("Cells:")
for fire in fires_seized:
    print(f" - {fire[1]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {water - remaining_water}")