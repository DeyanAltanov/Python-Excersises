def calculations(first_number, sign, second_number):
    if sign == '/':
        return f"{first_number / second_number:.2f}"
    elif sign == '*':
        return f"{first_number * second_number:.2f}"
    elif sign == '-':
        return f"{first_number - second_number:.2f}"
    elif sign == '+':
        return f"{first_number + second_number:.2f}"
    elif sign == '^':
        return f"{first_number ** second_number:.2f}"