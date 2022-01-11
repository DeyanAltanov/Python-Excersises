rows, columns = list(map(int, input().split(', ')))

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split(', '))))

best_sum = 0
best_submatrix = [[], []]

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if current_sum > best_sum:
            best_submatrix = [[str(matrix[i][j]), str(matrix[i][j + 1])], [str(matrix[i + 1][j]), str(matrix[i + 1][j + 1])]]
            best_sum = current_sum

print(f"{' '.join(best_submatrix[0])}")
print(f"{' '.join(best_submatrix[1])}")
print(best_sum)