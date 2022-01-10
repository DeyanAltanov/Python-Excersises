num = int(input())


def tribonacci_sequence(number):
    numbers = [1, 1, 2]
    if number == 0:
        print(0)
    elif 0 < number <= 3:
        print(1)
        for n in range(1, number):
            print(n)
    else:
        for n in range(2, number - 1):
            numbers.append(numbers[n] + numbers[n - 1] + numbers[n - 2])
        for n in range(0, len(numbers)):
            numbers[n] = str(numbers[n])
        print(' '.join(numbers))


tribonacci_sequence(num)