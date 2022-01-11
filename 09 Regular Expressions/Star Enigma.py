import re

messages_count = int(input())

messages = {}
decrypted_messages = []

for message in range(0, messages_count):
    new_message = input()
    messages[new_message] = 0
    for char in new_message:
        if char == 's' or char == 'S' or char == 't' or char == 'T' or char == 'a' or char == 'A' or char == 'r' or char == 'R':
            messages[new_message] += 1

for message in messages:
    decrypted_message = ''
    for char in message:
        decrypted_message += chr(ord(char) - messages[message])
    decrypted_messages.append(decrypted_message)

regex = r"\@([A-Za-z]+)([^\@\-\!\:\>]+)?\:([0-9]+)([^\@\-\!\:\>]+)?\!([A|D])\!([^\@\-\!\:\>]+)?\-\>([0-9]+)"
regex_name = r"(?<=@)[a-zA-Z]+"
regex_type = r"(?<=!)[A|D](?=!)"

planets = []
attacked_planets = []
destroyed_planets = []

for message in decrypted_messages:
    planet = re.finditer(regex, message)
    for name in planet:
        planets.append(name.group(0))

for p in planets:
    planet = re.findall(regex_name, p)
    type = re.findall(regex_type, p)
    if type[0] == 'A':
        attacked_planets.append(planet[0])
    else:
        destroyed_planets.append(planet[0])

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")