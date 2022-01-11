def odd_even(command, list):
    if command == 'Even':
        return sum(number for number in list if number % 2 == 0) * len(list)
    elif command == 'Odd':
        return sum(number for number in list if number % 2 == 1) * len(list)


print(odd_even(input(), [int(number) for number in input().split()]))