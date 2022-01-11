def permute(chars, current_index=0):
    if current_index == len(chars):
        print(''.join(chars))
        return

    for index in range(current_index, len(chars)):
        chars[current_index], chars[index] = chars[index], chars[current_index]
        permute(chars, current_index + 1)
        chars[current_index], chars[index] = chars[index], chars[current_index]


text = list(input())
permute(text)