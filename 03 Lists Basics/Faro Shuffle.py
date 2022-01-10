n = input()

shuffles = int(input())

deck = n.split(' ')
shuffled_deck = []

shuffle_1 = deck[:len(deck) // 2]
shuffle_2 = deck[len(deck) // 2:]

for i in range(shuffles):
    shuffled_deck = []
    shuffled_deck.append(deck[0])
    shuffle_1.remove(shuffle_1[0])
    shuffle_2.remove(shuffle_2[-1])
    for j in range(0, len(shuffle_1)):
        shuffled_deck.append(shuffle_2[j])
        shuffled_deck.append(shuffle_1[j])
    shuffled_deck.append(deck[-1])
    shuffle_1 = shuffled_deck[:len(deck) // 2]
    shuffle_2 = shuffled_deck[len(deck) // 2:]

print(shuffled_deck)