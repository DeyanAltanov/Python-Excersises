import re

text = input()

regex = r"www\.[a-zA-Z0-9\-]+\.[a-z\.]+"

all_emails = []

while text:
    email = re.findall(regex, text)
    if email:
        all_emails.extend(email)
    text = input()

for email in all_emails:
    print(email)