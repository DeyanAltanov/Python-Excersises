first_set = set()
second_set = set()
numbers = list(map(int, input().split()))

n = numbers[0]
m = numbers[1]

for _ in range(n):
    number = int(input())
    first_set.add(number)

for _ in range(m):
    number = int(input())
    second_set.add(number)

intersection_numbers = first_set.intersection(second_set)

for number in intersection_numbers:
    print(number)