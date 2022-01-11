def absolute(list):
    absolute_values = [abs(number) for number in list]
    return absolute_values


numbers = [float(number) for number in input().split()]

print(absolute(numbers))