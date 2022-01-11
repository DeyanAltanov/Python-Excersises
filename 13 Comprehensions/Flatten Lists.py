lists = input().split('|')
lists.reverse()

result = [number.strip() for number in range(len(lists)) for number in lists[number].split()]
print(*result)