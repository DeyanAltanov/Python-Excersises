import re

names = input()

regex = "\\b[A-Z][a-z]+\s[A-Z][a-z]+\\b"

matches = re.findall(regex, names)

print(' '.join(matches))