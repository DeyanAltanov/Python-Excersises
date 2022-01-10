one = int(input())
two = int(input())
three = int(input())


def multiply(first_number, second_number, third_number):
    numbers = [first_number, second_number, third_number]
    negatives = 0
    zero = False
    for number in range(0, len(numbers)):
        if numbers[number] < 0:
            negatives += 1
        if numbers[number] == 0:
            zero = True
    if zero is True:
        return 'zero'
    elif negatives == 2 or negatives == 0:
        return 'positive'
    else:
        return 'negative'


print(multiply(one, two, three))