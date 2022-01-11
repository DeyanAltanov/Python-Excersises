integers = list(map(int, input().split()))

reversed_integers = []

for integer in range(len(integers)):
    reversed_integers.append(integers.pop())

for integer in reversed_integers:
    print(integer, end=' ')