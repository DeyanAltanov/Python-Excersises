def expressions(numbers, current_sum=0, expression=''):
    if not numbers:
        return [(expression, current_sum)]

    result_plus = expressions(numbers[1:], current_sum + numbers[0], f"{expression}+{numbers[0]}")
    result_minus = expressions(numbers[1:], current_sum - numbers[0], f"{expression}-{numbers[0]}")
    return result_plus + result_minus


numbers = [int(number) for number in input().split(', ')]
print(*[f"{number[0]}={number[1]}" for number in expressions(numbers)], sep='\n')