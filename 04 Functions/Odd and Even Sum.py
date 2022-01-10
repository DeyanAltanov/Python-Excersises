num = input()


def odds_evens_sum(number):
    odds_sum = 0
    evens_sum = 0
    for digit in range(0, len(number)):
        if int(number[digit]) % 2 == 0:
            evens_sum += int(number[digit])
        else:
            odds_sum += int(number[digit])

    return f'Odd sum = {odds_sum}, Even sum = {evens_sum}'


print(odds_evens_sum(num))