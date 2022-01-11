car_count = int(input())
parking = set()

for _ in range(car_count):
    direction_and_car = input().split(', ')
    direction = direction_and_car[0]
    car = direction_and_car[1]
    if direction == 'IN':
        parking.add(car)
    else:
        parking.remove(car)

if len(parking) > 0:
    for car in parking:
        print(car)
else:
    print('Parking Lot is Empty')