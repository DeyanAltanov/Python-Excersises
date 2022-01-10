items = input()

budget = float(input())

m = items.split('|')

spent = 0
new = 0

n = []

sell_list = []

for i in range(len(m)):
    n.append(m[i].split('->'))

for i in range(len(n)):
    if n[i][0] == 'Clothes':
        if float(n[i][1]) <= 50.00 and budget - float(n[i][1]) >= 0:
            budget -= float(n[i][1])
            sell_list.append((float(n[i][1]) * 0.4) + float(n[i][1]))
            spent += float(n[i][1])
            new += (float(n[i][1]) * 0.4) + float(n[i][1])
    elif n[i][0] == 'Shoes':
        if float(n[i][1]) <= 35.00 and budget - float(n[i][1]) >= 0:
            budget -= float(n[i][1])
            sell_list.append((float(n[i][1]) * 0.4) + float(n[i][1]))
            spent += float(n[i][1])
            new += (float(n[i][1]) * 0.4) + float(n[i][1])
    elif n[i][0] == 'Accessories':
        if float(n[i][1]) <= 20.50 and budget - float(n[i][1]) >= 0:
            budget -= float(n[i][1])
            sell_list.append((float(n[i][1]) * 0.4) + float(n[i][1]))
            spent += float(n[i][1])
            new += (float(n[i][1]) * 0.4) + float(n[i][1])

for i in sell_list:
    print(f"{i:.2f} ", end="")
    budget += int(i)

print()
print(f"Profit: {new - spent:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")