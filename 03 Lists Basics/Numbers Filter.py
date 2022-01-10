n = int(input())
numbers = []
filtered_list = []

for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()

if command == "even":
    for i in numbers:
        if i % 2 == 0:
            filtered_list.append(i)
elif command == "odd":
    for i in numbers:
        if i % 2 == 1:
            filtered_list.append(i)
elif command == "positive":
    for i in numbers:
        if i >= 0:
            filtered_list.append(i)
elif command == "negative":
    for i in numbers:
        if i < 0:
            filtered_list.append(i)

print(filtered_list)