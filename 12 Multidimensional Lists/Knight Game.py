rows = int(input())

matrix = []
horses = 0

for _ in range(rows):
    matrix.append(list(input()))


def is_valid_bound(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


def calculate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]
        if is_valid_bound(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == 'K':
                kills += 1
    return kills


removed_knights = 0
while True:
    max_kills = 0
    killer_position = []
    for row_index in range(rows):
        for col_index in range(rows):
            if matrix[row_index][col_index] == 'K':
                kills = calculate_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row_index, col_index]

    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)