import re

text = input()
word = input()

pattern = f"\\b{word}\\b"

occurrences = re.findall(pattern, text, re.IGNORECASE)

print(len(occurrences))