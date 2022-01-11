rows, cols = list(map(int, input().split()))

matrix = []
player_position = [[], []]


def is_valid_bound(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False


for index in range(rows):
    matrix.append([])
    row = input()
    for char in range(len(row)):
        matrix[index].append(row[char])
        if row[char] == 'P':
            player_position[0] = index
            player_position[1] = char


command = input()
end = False
result = ''
for char in range(len(command)):
    if end:
        break
    if command[char] == 'U':
        if is_valid_bound(player_position[0] - 1, player_position[1]):
            if matrix[player_position[0] - 1][player_position[1]] == 'B':
                result = 'dead'
                player_position[0] -= 1
                end = True
            else:
                matrix[player_position[0] - 1][player_position[1]] = 'P'
                matrix[player_position[0]][player_position[1]] = '.'
                player_position[0] -= 1
        else:
            end = True
            result = 'won'
            matrix[player_position[0]][player_position[1]] = '.'
    elif command[char] == 'D':
        if is_valid_bound(player_position[0] + 1, player_position[1]):
            if matrix[player_position[0] + 1][player_position[1]] == 'B':
                result = 'dead'
                player_position[0] += 1
                end = True
            else:
                matrix[player_position[0] + 1][player_position[1]] = 'P'
                matrix[player_position[0]][player_position[1]] = '.'
                player_position[0] += 1
        else:
            end = True
            result = 'won'
            matrix[player_position[0]][player_position[1]] = '.'
    elif command[char] == 'L':
        if is_valid_bound(player_position[0], player_position[1] - 1):
            if matrix[player_position[0]][player_position[1] - 1] == 'B':
                result = 'dead'
                player_position[1] -= 1
                end = True
            else:
                matrix[player_position[0]][player_position[1] - 1] = 'P'
                matrix[player_position[0]][player_position[1]] = '.'
                player_position[1] -= 1
        else:
            end = True
            result = 'won'
            matrix[player_position[0]][player_position[1]] = '.'
    elif command[char] == 'R':
        if is_valid_bound(player_position[0], player_position[1] + 1):
            if matrix[player_position[0]][player_position[1] + 1] == 'B':
                end = True
                player_position[1] += 1
                result = 'dead'
            else:
                matrix[player_position[0]][player_position[1] + 1] = 'P'
                matrix[player_position[0]][player_position[1]] = '.'
                player_position[1] += 1
        else:
            end = True
            result = 'won'
            matrix[player_position[0]][player_position[1]] = '.'
    for row in range(rows):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'B':
                if is_valid_bound(row - 1, col):
                    if matrix[row - 1][col] == 'P':
                        result = 'dead'
                        end = True
                    matrix[row - 1][col] = 'b'
                if is_valid_bound(row + 1, col):
                    if matrix[row + 1][col] == 'P':
                        result = 'dead'
                        end = True
                    matrix[row + 1][col] = 'b'
                if is_valid_bound(row, col + 1):
                    if matrix[row][col + 1] == 'P':
                        result = 'dead'
                        end = True
                    matrix[row][col + 1] = 'b'
                if is_valid_bound(row, col - 1):
                    if matrix[row][col - 1] == 'P':
                        result = 'dead'
                        end = True
                    matrix[row][col - 1] = 'b'
    for row in range(rows):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'b':
                matrix[row][col] = 'B'

for row in matrix:
    print(f"{''.join(row)}")
print(f"{result}: {' '.join(list(map(str, player_position)))}")