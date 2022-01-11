from functools import reduce


def operate(operator, *args):
    if operator == '+':
        result = 0
        for number in args:
            result += number
    elif operator == '-':
        result = reduce(lambda a, b: a - b, args)
    elif operator == '*':
        result = 1
        for number in args:
            result *= number
    elif operator == '/':
        result = reduce(lambda a, b: a / b, args)
    return result