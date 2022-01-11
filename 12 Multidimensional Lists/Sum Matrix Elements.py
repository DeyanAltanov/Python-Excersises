rows, columns = list(map(int, input().split(', ')))

matrix = []
sum_all = 0

for i in range(rows):
    matrix.append(list(map(int, input().split(', '))))

for row in matrix:
    sum_all += sum(row)

print(sum_all)
print(matrix)