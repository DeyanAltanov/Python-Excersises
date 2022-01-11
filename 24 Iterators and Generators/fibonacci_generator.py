def fibonacci():
    previous_number = 0
    current_number = 1
    while True:
        yield previous_number
        previous_number, current_number = current_number, previous_number + current_number