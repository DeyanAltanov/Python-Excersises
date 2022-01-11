rows = int(input())

directions = input().split()

matrix = []
position = [[], []]
coals = 0


def is_valid_bound(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


for index in range(rows):
    command = input().split()
    matrix.append(list(command))
    if 's' in command:
        position[0] = index
        position[1] = command.index('s')
    for coal in range(len(command)):
        if command[coal] == 'c':
            coals += 1

gg = False
s_row = int(position[0])
s_col = int(position[1])

for direction in directions:
    if direction == 'up':
        if is_valid_bound(s_row - 1, s_col):
            if matrix[s_row - 1][s_col] == 'c':
                coals -= 1
                matrix[s_row][s_col] = '*'
                s_row = int(s_row - 1)
                s_col = int(s_col)
            elif matrix[s_row - 1][s_col] == 'e':
                print(f"Game over! ({s_row - 1}, {s_col})")
                gg = True
                break
            else:
                matrix[s_row][s_col] = '*'
                s_row = int(s_row - 1)
                s_col = int(s_col)
    elif direction == 'down':
        if is_valid_bound(s_row + 1, s_col):
            if matrix[s_row + 1][s_col] == 'c':
                coals -= 1
                matrix[s_row][s_col] = '*'
                s_row = int(s_row + 1)
                s_col = int(s_col)
            elif matrix[s_row + 1][s_col] == 'e':
                print(f"Game over! ({s_row + 1}, {s_col})")
                gg = True
                break
            else:
                matrix[s_row][s_col] = '*'
                s_row = int(s_row + 1)
                s_col = int(s_col)
    elif direction == 'right':
        if is_valid_bound(s_row, s_col + 1):
            if matrix[s_row][s_col + 1] == 'c':
                coals -= 1
                matrix[s_row][s_col] = '*'
                s_row = int(s_row)
                s_col = int(s_col + 1)
            elif matrix[s_row][s_col + 1] == 'e':
                print(f"Game over! ({s_row}, {s_col + 1})")
                gg = True
                break
            else:
                matrix[s_row][s_col] = '*'
                s_row = int(s_row)
                s_col = int(s_col + 1)
    elif direction == 'left':
        if is_valid_bound(s_row, s_col - 1):
            if matrix[s_row][s_col - 1] == 'c':
                coals -= 1
                matrix[s_row][s_col] = '*'
                s_row = int(s_row)
                s_col = int(s_col - 1)
            elif matrix[s_row][s_col - 1] == 'e':
                print(f"Game over! ({s_row}, {s_col - 1})")
                gg = True
                break
            else:
                matrix[s_row][s_col] = '*'
                s_row = int(s_row)
                s_col = int(s_col - 1)
    if coals == 0:
        print(f"You collected all coals! ({s_row}, {s_col})")
        gg = True
        break

if not gg:
    print(f"{coals} coals left. ({s_row}, {s_col})")