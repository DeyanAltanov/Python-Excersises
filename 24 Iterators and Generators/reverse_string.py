def reverse_text(word):
    word = word[::-1]
    index = 0
    while index < len(word):
        yield word[index]
        index += 1