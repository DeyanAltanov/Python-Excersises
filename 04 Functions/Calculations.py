n = input()
a = int(input())
b = int(input())


def calculation(operator, first, second):
    if operator == 'multiply':
        return int(first * second)
    elif operator == 'divide':
        return int(first / second)
    elif operator == 'add':
        return int(first + second)
    elif operator == 'subtract':
        return int(first - second)


print(calculation(n, a, b))