def triangulate(number):
    for row in range(1, number + 1):
        for digit in range(1, row + 1):
            print(f"{digit}", end=' ')
        print()
    for row in range(number - 1, 0, -1):
        for digit in range(1, row + 1):
            print(f"{digit}", end=' ')
        print()