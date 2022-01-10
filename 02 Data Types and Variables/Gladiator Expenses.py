lostFightsCount = int(input())
helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

expenses = 0
brokenShields = 0

for losses in range(1, lostFightsCount + 1):
    if losses % 2 == 0:
        expenses += helmetPrice
    if losses % 3 == 0:
        expenses += swordPrice
    if losses % 2 == 0 and losses % 3 == 0:
        expenses += shieldPrice
        brokenShields += 1
    if brokenShields == 2:
        expenses += armorPrice
        brokenShields = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")