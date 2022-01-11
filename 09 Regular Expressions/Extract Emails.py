import re

text = input()

valid_emails = []

regex = r"(^|(?<=\s))([a-zA-Z][\w|\-|\.]+@[a-zA-Z][\w|\-|\.]+\.\w+\b)"

emails = re.finditer(regex, text)

for email in emails:
    valid_emails.append(email.group(0))

for email in valid_emails:
    print(email)