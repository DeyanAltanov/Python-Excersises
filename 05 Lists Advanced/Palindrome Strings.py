strings = input().split()
palindrome = input()

palindromes = [pal for pal in strings if pal == pal[::-1]]

result = 0

for pal in palindromes:
    if pal == palindrome:
        result += 1

print(palindromes)
print(f'Found palindrome {result} times')