neighborhood = [int(el) for el in input().split('@')]

command = input().split()
value = int(command[1])
current_index = 0

while not command[0] == 'Love!':
    value = int(command[1])
    current_index += value
    if current_index > len(neighborhood) - 1:
        if neighborhood[0] == 0:
            current_index = 0
            print(f"Place {current_index} already had Valentine's day.")
        else:
            current_index = 0
            neighborhood[0] -= 2
            if neighborhood[0] - 2 < 0:
                print(f"Place {current_index} has Valentine's day.")
                neighborhood[0] = 0
    else:
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood[current_index] -= 2
            if neighborhood[current_index] - 2 < 0:
                print(f"Place {current_index} has Valentine's day.")
                neighborhood[current_index] = 0

    command = input().split()


if all([value == 0 for value in neighborhood]):
    print(f"Cupid's last position was {current_index}.")
    print('Mission was successful.')
else:
    failed_places = 0
    for place in neighborhood:
        if place > 0:
            failed_places += 1
    print(f"Cupid's last position was {current_index}.")
    print(f'Cupid has failed {failed_places} places.')