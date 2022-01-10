key = int(input())
characters = int(input())
string = ''

for i in range(0, characters):
    char = input()
    n = ord(char) + key
    m = chr(n)
    string += m

print(string)