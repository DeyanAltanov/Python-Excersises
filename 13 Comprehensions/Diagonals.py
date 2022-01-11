matrix = [[int(el) for el in input().split(', ')] for col in range(int(input()))]

first_diagonal = [matrix[element][element] for element in range(len(matrix))]

for col in matrix:
    col.reverse()

second_diagonal = [matrix[element][element] for element in range(len(matrix))]

print(*[f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}"])
print(*[f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}"])