num = int(input())


def perfect_number(number):
    numbers = []
    for numb in range(1, number):
        if number % numb == 0:
            numbers.append(numb)
    if sum(numbers) == number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


print(perfect_number(num))