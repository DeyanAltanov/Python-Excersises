rows = int(input())


def is_valid_bound(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


matrtix = [list(map(int, input().split())) for row in range(rows)]

command = input().split()

while command[0] != 'END':
    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if is_valid_bound(row, col):
        if action == 'Add':
            matrtix[row][col] += value
        else:
            matrtix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input().split()

for row in matrtix:
    print(f"{' '.join([str(number) for number in row])}")