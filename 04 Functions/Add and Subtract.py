one = int(input())
two = int(input())
three = int(input())


def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract_numbers(first_number, second_number):
    return first_number - second_number


print(subtract_numbers(sum_numbers(one, two), three))