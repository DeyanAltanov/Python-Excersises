elements_count = int(input())

matrix = []
diagonal_sum = 0

for i in range(elements_count):
    matrix.append(list(map(int, input().split())))

for i in range(elements_count):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)