n = int(input())
word = input()

words = []
ws = []

for i in range(n):
    w = input()
    words.append(w)

for w in words:
    if w.find(word) != -1:
        ws.append(w)

print(words)
print(ws)