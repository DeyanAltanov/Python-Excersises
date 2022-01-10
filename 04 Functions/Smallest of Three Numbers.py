one = int(input())
two = int(input())
three = int(input())


def smallest_number(first_number, second_number, third_number):
    return min(first_number, second_number, third_number)


print(smallest_number(one, two, three))