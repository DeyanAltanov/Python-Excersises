command = input()
thing = input()

if command == 'int':
    print(int(thing) * 2)
elif command == 'real':
    print(f'{float(thing) * 1.5:.2f}')
else:
    print(f'${thing}$')