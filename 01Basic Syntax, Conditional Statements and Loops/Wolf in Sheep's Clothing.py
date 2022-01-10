queue = input()

list = queue.split(", ")
list.reverse()
eat = False
animal = 0
elements = len(list)

for a in range(len(list)):
    if list[0] == 'wolf':
        break
    if list[a + 1] == 'wolf':
        eat = True
        animal = a + 1
        break

if eat:
    print(f"Oi! Sheep number {animal}! You are about to be eaten by a wolf!")
else:
    print("Please go away and stop eating my sheep")