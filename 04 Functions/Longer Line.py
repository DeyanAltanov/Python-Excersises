x_first = []
y_first = []
x_second = []
y_second = []

for i in range(0, 2):
    one = float(input())
    x_first.append(one)
    two = float(input())
    y_first.append(two)
for i in range(0, 2):
    one = float(input())
    x_second.append(one)
    two = float(input())
    y_second.append(two)

first_distance = abs(pow((pow((x_first[0] + x_first[1]), 2) + pow((y_first[0] + y_first[1]), 2)), 0.5))
second_distance = abs(pow((pow((x_second[0] + x_second[1]), 2) + pow((y_second[0] + y_second[1]), 2)), 0.5))


if first_distance >= second_distance:
    print(f"({int(x_first[0])}, {int(y_first[0])})({int(x_first[1])}, {int(y_first[1])})")
else:
    print(f"({int(x_second[1])}, {int(y_second[1])})({int(x_second[0])}, {int(y_second[0])})")