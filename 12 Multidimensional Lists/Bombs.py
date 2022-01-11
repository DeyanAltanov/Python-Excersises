rows = int(input())

matrix = []
alive_cells = 0
alive_cells_sum = 0


def is_valid_bound(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


for _ in range(rows):
    matrix.append(list(map(int, input().split())))

explosions = input().split()

for explosion in explosions:
    row, col = list(map(int, explosion.split(',')))
    if matrix[row][col] > 0:
        if is_valid_bound(row - 1, col - 1) and matrix[row - 1][col - 1] > 0:
            matrix[row - 1][col - 1] -= matrix[row][col]
        if is_valid_bound(row - 1, col) and matrix[row - 1][col] > 0:
            matrix[row - 1][col] -= matrix[row][col]
        if is_valid_bound(row - 1, col + 1) and matrix[row - 1][col + 1] > 0:
            matrix[row - 1][col + 1] -= matrix[row][col]
        if is_valid_bound(row, col - 1) and matrix[row][col - 1] > 0:
            matrix[row][col - 1] -= matrix[row][col]
        if is_valid_bound(row, col + 1) and matrix[row][col + 1] > 0:
            matrix[row][col + 1] -= matrix[row][col]
        if is_valid_bound(row + 1, col - 1) and matrix[row + 1][col - 1] > 0:
            matrix[row + 1][col - 1] -= matrix[row][col]
        if is_valid_bound(row + 1, col) and matrix[row + 1][col] > 0:
            matrix[row + 1][col] -= matrix[row][col]
        if is_valid_bound(row + 1, col + 1) and matrix[row + 1][col + 1] > 0:
            matrix[row + 1][col + 1] -= matrix[row][col]
        matrix[row][col] -= matrix[row][col]

for row in matrix:
    for value in row:
        if value > 0:
            alive_cells += 1
            alive_cells_sum += value

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
for row in matrix:
    print(f"{' '.join(str(i) for i in row)}")