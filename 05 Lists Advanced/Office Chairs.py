rooms = int(input())
free_chairs = 0
no = False

for room in range(1, rooms + 1):
    chairs = input().split(' ')
    all_chairs = chairs[0]
    used_chairs = int(chairs[1])
    if used_chairs - len(all_chairs) > 0:
        print(f"{used_chairs - len(all_chairs)} more chairs needed in room {room}")
        no = True
    elif used_chairs - len(all_chairs) < 0:
        free_chairs += len(all_chairs) - used_chairs

if not no:
    print(f"Game On, {free_chairs} free chairs left")