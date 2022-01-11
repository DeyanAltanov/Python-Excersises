words = input().lower().split()

occurrences = []

for word in words:
    if words.count(word) % 2 == 1:
        if word not in occurrences:
            occurrences.append(word)

print(' '.join(occurrences))