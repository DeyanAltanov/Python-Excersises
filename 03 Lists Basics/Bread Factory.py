day_events = input()
energy = 100
coins = 100
bankrupt = False

events = day_events.split('|')
e = []

for i in range(len(events)):
    e.append(events[i].split('-'))

for i in range(len(e)):
    if e[i][0] == 'rest':
        if energy + int(e[i][1]) > 100:
            print("You gained 0 energy.")
            print(f"Current energy: {energy}.")
        else:
            energy += int(e[i][1])
            print(f"You gained {int(e[i][1])} energy.")
            print(f"Current energy: {energy}.")
    elif e[i][0] == 'order':
        if energy - 30 < 0:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += int(e[i][1])
            print(f"You earned {int(e[i][1])} coins.")
    else:
        if coins - int(e[i][1]) >= 0:
            print(f"You bought {e[i][0]}.")
            coins -= int(e[i][1])
        else:
            print(f"Closed! Cannot afford {e[i][0]}.")
            bankrupt = True
            break

if not bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")