elements = int(input())

matrix = []

for i in range(elements):
    row = input()
    matrix.append([])
    for char in row:
        matrix[i].append(char)

symbol = input()
equal = False

for row in range(len(matrix)):
    for element in range(len(matrix[row])):
        if matrix[row][element] == symbol:
            print(f"({row}, {element})")
            equal = True
            break
    if equal is True:
        break

if not equal:
    print(f"{symbol} does not occur in the matrix")