from sequence import fibonacci_sequence, number_locator

info = input().split()

command = info[0]

while command != 'Stop':
    if command == 'Create':
        sequence = fibonacci_sequence(int(info[2]))
        print(f"{' '.join(str(number) for number in sequence)}")
    elif command == 'Locate':
        print(number_locator(int(info[1]), sequence))

    info = input().split()
    command = info[0]