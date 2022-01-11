s = input()
ss = ""

for i in range(0, len(s)):
    ss += s[i]
    for j in range(i, i + 1):
        ss += s[j]

print(ss)