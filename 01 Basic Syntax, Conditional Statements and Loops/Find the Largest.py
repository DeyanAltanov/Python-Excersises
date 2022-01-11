number = input()
list = []
result = ''

for digit in number:
    list.append(digit)

list.sort(reverse=True)

print(result.join(list))