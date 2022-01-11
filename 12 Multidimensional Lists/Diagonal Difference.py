elements_count = int(input())

matrix = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(elements_count):
    matrix.append(list(map(int, input().split())))

for i in range(elements_count):
    primary_diagonal_sum += matrix[i][i]

for i in range(elements_count):
    matrix[i].reverse()
    secondary_diagonal_sum += matrix[i][i]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))