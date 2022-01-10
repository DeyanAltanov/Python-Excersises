n = input()
m = input()
r = list(n)
p = ""

for i in range(0, len(m)):
    p = "".join(r)
    r[i] = m[i]
    n = "".join(r)
    if n != p:
        print(n)