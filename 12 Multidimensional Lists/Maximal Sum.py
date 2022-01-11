rows, cols = list(map(int, input().split()))
max_sum = 0
best_3_x_3 = [[], [], []]

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

for i in range(rows - 2):
    for j in range(cols - 2):
        if matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2] > max_sum:
            max_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
            best_3_x_3 = [[], [], []]
            best_3_x_3[0].append(matrix[i][j])
            best_3_x_3[0].append(matrix[i][j + 1])
            best_3_x_3[0].append(matrix[i][j + 2])
            best_3_x_3[1].append(matrix[i + 1][j])
            best_3_x_3[1].append(matrix[i + 1][j + 1])
            best_3_x_3[1].append(matrix[i + 1][j + 2])
            best_3_x_3[2].append(matrix[i + 2][j])
            best_3_x_3[2].append(matrix[i + 2][j + 1])
            best_3_x_3[2].append(matrix[i + 2][j + 2])

print(f"Sum = {max_sum}")
for row in best_3_x_3:
    for number in range(len(row)):
        row[number] = str(row[number])
    print(f"{' '.join(row)}")