n = int(input())
sum = 0

for i in range(0, n):
    char = input()
    sum += ord(char)

print(f"The sum equals: {sum}")