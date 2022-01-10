n = input()

numbs = n.split(', ')


def palindromes(numbers):
    for element in range(0, len(numbers)):
        el = numbers[element]
        rev = ''.join(reversed(el))
        if el == rev:
            print(True)
        else:
            print(False)


palindromes(numbs)