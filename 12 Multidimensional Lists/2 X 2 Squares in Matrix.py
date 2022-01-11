rows, cols = list(map(int, input().split()))
equal_squares = 0

matrix = []

for i in range(rows):
    matrix.append(list(input().split()))

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            equal_squares += 1

print(equal_squares)