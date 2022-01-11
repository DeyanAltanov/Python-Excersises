strings = input().split()

string_1 = strings[0]
string_2 = strings[1]
sum = 0

minimum_length = min(len(string_1), len(string_2))

maximum_length = max(len(string_1), len(string_2))

difference = maximum_length - minimum_length

for index in range(0, minimum_length):
    sum += ord(string_1[index]) * ord(string_2[index])

for index in range(maximum_length - 1, (maximum_length - difference) - 1, -1):
    if len(string_1) > len(string_2):
        sum += ord(string_1[index])
    else:
        sum += ord(string_2[index])

print(sum)