x = []
y = []
for i in range(0, 2):
    one = float(input())
    x.append(one)
    two = float(input())
    y.append(two)

first_result = abs(x[0]) + abs(y[0])
second_result = abs(x[1]) + abs(y[1])

if first_result > second_result:
    print(f"({int(x[1])}, {int(y[1])})")
else:
    print(f"({int(x[0])}, {int(y[0])})")