elements = int(input())

numbers = [map(int, input().split(', ')) for _ in range(elements)]
matrix = [[x for x in number if x % 2 == 0] for number in numbers]

print(matrix)