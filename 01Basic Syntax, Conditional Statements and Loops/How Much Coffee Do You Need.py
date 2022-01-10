event = input()
coffees = 0
capital = False

while not event == 'END':
    string = event.lower()
    if string == 'coding' or string == 'cat' or string == 'dog' or string == 'movie':
        for char in event:
            letter = ord(char)
            if letter in range(65, 90):
                capital = True
                break
        if capital:
            coffees += 2
        else:
            coffees += 1

    event = input()
    capital = False

if coffees < 5:
    print(coffees)
else:
    print('You need extra sleep')