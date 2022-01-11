import re

all_text = input()

text = ""

for char in range(len(all_text)):
    text += all_text[char]

regex_title = r"(?<=\<title\>)[\s\S]+(?=\<\/title\>)"
regex_body = r"(?<=\<body\>)[\s\S]+(?=\<\/body\>)"
regex_tag = r'(<[^>]*>)'

title_list = re.findall(regex_title, text)
body_list = re.findall(regex_body, text)

title = title_list[0]
body = body_list[0]

b = re.compile(regex_tag)
new_body = b.sub('', body)
new_body = new_body.replace('\\n', '')
new_body = new_body.strip()

print(f"Title: {title}")
print(f"Content: {new_body}")