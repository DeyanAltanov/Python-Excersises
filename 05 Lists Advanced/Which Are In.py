first_list = input().split(', ')
second_list = input().split(', ')
result = []

for string in first_list:
    for word in second_list:
        if string in word:
            if string not in result:
                result.append(string)

print(result)