text = input()
n = int(input())


def repeat_string(word, repeat):
    maikati = ''
    for i in range(0, repeat):
        maikati += word

    return maikati


print(repeat_string(text, n))