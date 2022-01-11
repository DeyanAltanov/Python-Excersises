def genrange(start, end):
    current_number = int(start)
    while current_number <= int(end):
        yield current_number
        current_number += 1