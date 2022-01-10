all_cards = input()

a = 11
b = 11
A = []
B = []

cards = all_cards.split(' ')

for card in cards:
    player = card.split('-')
    if player[0] == 'A' and player[1] not in A:
        a -= 1
        A.append(player[1])
        if a < 7:
            print(f"Team A - {a}; Team B - {b}")
            print('Game was terminated')
            break
    elif player[0] == 'B' and player[1] not in B:
        b -= 1
        B.append(player[1])
        if b < 7:
            print(f"Team A - {a}; Team B - {b}")
            print('Game was terminated')
            break

if a >= 7 and b >= 7:
    print(f"Team A - {a}; Team B - {b}")