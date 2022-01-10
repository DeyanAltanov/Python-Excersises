year = input()
x = True

while x:
    y = 0
    year = int(year)
    year += 1
    year = str(year)
    for i in range(0, len(year)):
        for j in range(i + 1, len(year)):
            if year[i] == year[j]:
                y = 1
                break
    if y == 0:
        print(year)
        x = False
        break