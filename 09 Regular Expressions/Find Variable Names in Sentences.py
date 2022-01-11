import re

text = input()

regex = r"\b_{1}([a-zA-Z]+|\d+)\b"

variables = re.findall(regex, text)

print(','.join(variables))