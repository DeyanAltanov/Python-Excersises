n = int(input())
litres = 0

for i in range(1, n + 1):
    pour = int(input())
    if 255 - (litres + pour) < 0:
        print("Insufficient capacity!")
    else:
        litres += pour

print(litres)