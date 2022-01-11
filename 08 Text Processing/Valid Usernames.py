usernames = input().split(', ')

for username in usernames:
    if 3 <= len(username) <= 16:
        name = True
        for char in range(len(username)):
            if username[char].isdigit() or username[char].isalpha() or username[char] == '-' or username[char] == '_':
                pass
            else:
                name = False
        if name is True:
            print(username)