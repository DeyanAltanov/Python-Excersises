user_side = input()
forcebook = {}

while user_side != 'Lumpawaroo':
    if '|' in user_side:
        side_user = user_side.split(' | ')
        side = side_user[0]
        user = side_user[1]
        if side not in forcebook:
            forcebook[side] = []
        if any(user in value for value in forcebook.values()) is False:
            forcebook[side].append(user)
    elif '>' in user_side:
        side_user = user_side.split(' -> ')
        side = side_user[1]
        user = side_user[0]
        for force, users in forcebook.items():
            if user in users:
                users.remove(user)
                break
        if side not in forcebook:
            forcebook[side] = [user]
            print(f"{user} joins the {side} side!")
        elif side in forcebook and user not in forcebook[side]:
            forcebook[side].append(user)
            print(f"{user} joins the {side} side!")

    user_side = input()

forcebook = dict(sorted(forcebook.items(), key=lambda x: x))
forcebook = dict(sorted(forcebook.items(), key=lambda x: len(x[1]), reverse=True))

for side in forcebook:
    if len(forcebook[side]) > 0:
        print(f"Side: {side}, Members: {len(forcebook[side])}")
        forcebook[side].sort()
        for user in forcebook[side]:
            print(f"! {user}")