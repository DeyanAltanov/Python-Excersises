n = int(input())

users = {}

for i in range(0, n):
    information = input().split()
    action = information[0]
    user = information[1]

    if action == 'register':
        car = information[2]
        if user not in users:
            users[user] = car
            print(f"{user} registered {car} successfully")
        else:
            print(f"ERROR: already registered with plate number {car}")
    else:
        if user not in users:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            users.pop(user)

for user in users:
    print(f"{user} => {users[user]}")