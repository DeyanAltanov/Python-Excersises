a = int(input())
b = int(input())


def factorial_division(n, m):
    first_factorial = 1
    second_factorial = 1
    for i in range(1, n + 1):
        first_factorial *= i
    for i in range(1, m + 1):
        second_factorial *= i

    return f"{(first_factorial / second_factorial):.2f}"


print(factorial_division(a, b))