def squares(number):
    current_number = 1
    while current_number <= int(number):
        yield int(pow(current_number, 2))
        current_number += 1