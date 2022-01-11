rows, columns = list(map(int, input().split(', ')))

matrix = []
sum_columns = [0] * columns

for i in range(rows):
    matrix.append(list(map(int, input().split())))

for column in matrix:
    for number in range(len(column)):
        sum_columns[number] += column[number]

for number in sum_columns:
    print(number)