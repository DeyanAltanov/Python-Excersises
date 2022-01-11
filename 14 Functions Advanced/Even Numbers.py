def filter_even_numbers(numbers):
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    return evens


numbers = [int(number) for number in input().split()]

print(filter_even_numbers(numbers))