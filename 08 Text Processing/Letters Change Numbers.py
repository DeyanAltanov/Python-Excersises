alphabet_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

inputs = input().split()
result = 0

for word in inputs:
    first_letter = word[0]
    last_letter = word[-1]
    number = float(word[1:][:-1])
    resulted_number = 0
    if first_letter.isupper() is True:
        resulted_number += number / (alphabet_2.index(first_letter) + 1)
    else:
        resulted_number += number * (alphabet_1.index(first_letter) + 1)
    if last_letter.isupper() is True:
        resulted_number -= (alphabet_2.index(last_letter) + 1)
    else:
        resulted_number += (alphabet_1.index(last_letter) + 1)
    result += resulted_number

print(f"{result:.2f}")