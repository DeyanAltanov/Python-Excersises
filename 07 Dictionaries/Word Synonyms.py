count = int(input())
word_synonyms = {}

for number in range(count):
    key = input()
    synonym = input()
    if key not in word_synonyms:
        word_synonyms[key] = []
    word_synonyms[key].append(synonym)

for word in word_synonyms:
    print(f"{word} - {', '.join(word_synonyms[word])}")