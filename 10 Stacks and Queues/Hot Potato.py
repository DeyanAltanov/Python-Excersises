from collections import deque

children = input().split()
toss = int(input())
players = deque(children)
counter = 0

while len(players) > 1:
    counter += 1
    current_player = players.popleft()
    if counter == toss:
        print(f"Removed {current_player}")
        counter = 0
    else:
        players.append(current_player)

print(f"Last is {players[0]}")