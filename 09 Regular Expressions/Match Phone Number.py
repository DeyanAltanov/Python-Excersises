import re

all_phones = input()
telephones = []

regex = "(\+359\s2\s\d{3}\s\d{4}\\b)|(\+359-2-\d{3}-\d{4}\\b)"
phones = re.finditer(regex, all_phones)

for phone in phones:
    telephones.append(phone.group(0))

print(', '.join(telephones))