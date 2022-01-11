def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        numbers = []
        current = 0
        for number in seq:
            numbers.append(number)
            current += 1
            if current >= n:
                break
        return numbers

    return take, halves, integers