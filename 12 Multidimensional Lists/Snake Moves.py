rows, cols = list(map(int, input().split()))

matrix = []

for i in range(rows):
    matrix.append(list(cols * ' '))

snake = input()
snake_left = 0

if len(snake) >= len(matrix[0]):
    for i in range(len(matrix[0])):
        matrix[0][i] = snake[i]
        snake_left += 1
else:
    for i in range(len(matrix[0])):
        matrix[0][i] = snake[snake_left]
        snake_left += 1
        if snake_left == len(snake):
            snake_left = 0

for i in range(1, len(matrix)):
    if i % 2 == 1:
        for j in range(len(matrix[i]) - 1, -1, -1):
            if snake_left == len(snake):
                snake_left = 0
                matrix[i][j] = snake[snake_left]
                snake_left += 1
            elif snake_left < len(snake):
                matrix[i][j] = snake[snake_left]
                snake_left += 1
            else:
                matrix[i][j] = snake[snake_left]
                snake_left += 1
    else:
        for j in range(len(matrix[i])):
            if snake_left == len(snake):
                snake_left = 0
                matrix[i][j] = snake[snake_left]
                snake_left += 1
            elif snake_left < len(snake):
                matrix[i][j] = snake[snake_left]
                snake_left += 1
            else:
                matrix[i][j] = snake[snake_left]
                snake_left += 1

for row in matrix:
    print(f"{''.join(row)}")