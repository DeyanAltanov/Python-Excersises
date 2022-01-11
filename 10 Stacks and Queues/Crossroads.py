from collections import deque

original_duration = int(input())
original_free_window = int(input())
duration = original_duration
free_window = original_free_window
crossroad = deque()
passed_cars = 0
crash = False

command = input()

while command != 'END':
    if command != 'green' and duration > 0:
        for char in command:
            crossroad.append(char)
        for char in range(duration):
            if crossroad:
                crossroad.popleft()
                duration -= 1
        if duration == 0 and crossroad:
            for char in range(free_window):
                if crossroad:
                    crossroad.popleft()
                    free_window -= 1
            if free_window == 0 and crossroad:
                crash = crossroad.popleft()
                print('A crash happened!')
                print(f"{command} was hit at {crash}.")
                crash = True
                break
        passed_cars += 1
    else:
        duration = original_duration
        free_window = original_free_window
    command = input()

if not crash:
    print('Everyone is safe.')
    print(f"{passed_cars} total cars passed the crossroads.")