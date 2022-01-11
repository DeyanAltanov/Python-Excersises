clothes = list(map(int, input().split()))

capacity = int(input())

racks = 0

sum = 0

for c in range(len(clothes)):
    clothing = clothes.pop()
    sum += clothing
    if sum == capacity:
        racks += 1
        sum = 0
    elif len(clothes) > 0:
        if sum + clothes[-1] > capacity:
            racks += 1
            sum = 0
    else:
        racks += 1

print(racks)