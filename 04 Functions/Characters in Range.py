a = input()
b = input()


def chars_in_range(first_char, second_char):
    text = ''
    for char in range(ord(first_char) + 1, ord(second_char)):
        text += chr(char)
        text += ' '

    return text


print(chars_in_range(a, b))