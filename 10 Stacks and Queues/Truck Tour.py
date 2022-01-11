from collections import deque

pumps_count = int(input())
litters = deque()
distances = deque()

for pump in range(pumps_count):
    petrol_distance = list(map(int, input().split()))
    petrol = petrol_distance[0]
    distance = petrol_distance[1]
    litters.append(petrol)
    distances.append(distance)

original_litters = list(litters)
original_distances = list(distances)
full_circle = False

while full_circle is False:
    tank_litters = 0
    circles = 0
    for i in range(0, pumps_count):
        pump_litters = litters.popleft()
        distance_next_pump = distances.popleft()
        litters.append(pump_litters)
        distances.append(distance_next_pump)
        tank_litters += pump_litters
        if tank_litters < distance_next_pump:
            break
        else:
            tank_litters -= distance_next_pump
            circles += 1


    if circles == pumps_count:
        full_circle = True

best_pump = str(litters.popleft())
best_distance = str(distances.popleft())
best_of_the_best = best_pump + ' ' + best_distance

original_litters_strings = [str(integer) for integer in original_litters]
original_distances_strings = [str(integer) for integer in original_distances]

original_pumps = []

for index in range(len(original_distances_strings)):
    original_pumps.append(original_litters_strings[index] + ' ' + original_distances_strings[index])

for pump in range(len(original_pumps)):
    if original_pumps[pump] == best_of_the_best:
        print(pump)
        break