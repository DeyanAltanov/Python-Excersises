def fibonacci_sequence(number):
    sequence = []
    if number == 1:
        sequence.append(0)
    elif number == 2:
        sequence.append(0)
        sequence.append(1)
    elif number >= 3:
        sequence.append(0)
        sequence.append(1)
        for num in range(2, number):
            sequence.append(sequence[num - 2] + sequence[num - 1])
    return sequence


def number_locator(number, sequence):
    if number in sequence:
        return f"The number - {number} is at index {sequence.index(number)}"
    else:
        return f"The number {number} is not in the sequence"