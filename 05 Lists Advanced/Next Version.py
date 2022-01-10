version = [int(el) for el in input().split('.')]

if version[1] == 9 and version[2] == 9:
    version[0] += 1
    version[1] = 0
    version[2] = 0
else:
    if version[2] == 9:
        version[2] = 0
    else:
        version[2] += 1
    if version[2] == 0 and version[1] + 1 == 10:
        version[1] = 0
    elif version[2] == 0:
        version[1] += 1

print(f"{version[0]}.{version[1]}.{version[2]}")