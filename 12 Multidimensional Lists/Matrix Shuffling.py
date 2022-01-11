rows, cols = input().split()

matrix = []

for i in range(int(rows)):
    col = input().split()
    matrix.append([])
    for value in range(len(col)):
        matrix[i].append(col[value])

command_info = input().split()
command = command_info[0]

while command != 'END':
    if command != 'swap' or len(command_info) != 5:
        print('Invalid input!')
    else:
        row_1 = int(command_info[1])
        col_1 = int(command_info[2])
        row_2 = int(command_info[3])
        col_2 = int(command_info[4])
        if row_1 > len(matrix) - 1 or row_2 > len(matrix) - 1 or col_1 > len(matrix[0]) - 1 or col_2 > len(matrix[0]) - 1:
            print('Invalid input!')
            command_info = input().split()
            command = command_info[0]
            continue
        first_value = matrix[row_1][col_1]
        second_value = matrix[row_2][col_2]
        matrix[row_1][col_1] = second_value
        matrix[row_2][col_2] = first_value
        for row in matrix:
            print(f"{' '.join(row)}")
    command_info = input().split()
    command = command_info[0]