words = input().split()

message = []

for word in words:
    if 2 >= len(word):
        message.append(chr(int(word[0] + word[1])))
    elif len(word) == 3:
        if '0' <= word[2] <= '9':
            letter_one = word[0] + word[1] + word[2]
            first_letter = chr(int(letter_one))
            message.append(first_letter)
        else:
            letter_one = word[0] + word[1]
            first_letter = chr(int(letter_one))
            phrase = ''
            phrase += first_letter
            phrase += word[-1]
            message.append(phrase)
    elif '0' <= word[2] <= '9':
        letter_one = word[0] + word[1] + word[2]
        first_letter = chr(int(letter_one))
        second_letter = word[-1]
        phrase = ''
        phrase += first_letter
        phrase += second_letter
        last_letter = word[3]
        for w in range(4, len(word) - 1):
            phrase += word[w]
        if len(word) > 4:
            phrase += last_letter
        message.append(phrase)
    else:
        letter_one = word[0] + word[1]
        first_letter = chr(int(letter_one))
        second_letter = word[-1]
        phrase = ''
        phrase += first_letter
        phrase += second_letter
        last_letter = word[2]
        for w in range(3, len(word) - 1):
            phrase += word[w]

        phrase += last_letter
        message.append(phrase)

print(' '.join(message))