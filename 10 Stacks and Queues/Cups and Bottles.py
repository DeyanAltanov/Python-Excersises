from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))
wasted_litres = 0

while True:
    if len(cups) > 0 and len(bottles) > 0:
        first_cup = cups.popleft()
        while first_cup > 0:
            if len(bottles) > 0:
                last_bottle = bottles.pop()
                if last_bottle == first_cup:
                    first_cup = 0
                elif last_bottle > first_cup:
                    wasted_litres += last_bottle - first_cup
                    first_cup = 0
                elif last_bottle < first_cup:
                    first_cup = abs(last_bottle - first_cup)
            else:
                break
    else:
        break

if len(bottles) > 0:
    print("Bottles: ", end='')
    for bottle in bottles:
        print(f"{bottle} ", end='')
elif len(cups) > 0:
    print("Cups: ", end='')
    for cup in cups:
        print(f"{cup} ", end='')
print()
print(f"Wasted litters of water: {wasted_litres}")