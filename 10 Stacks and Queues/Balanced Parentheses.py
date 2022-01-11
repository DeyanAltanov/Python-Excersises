sequence = input()
balanced = True
opening_brackets = []

values = {'{': '}', '[': ']', '(': ')'}

for char in sequence:
    if char in "{[(":
        opening_brackets.append(char)
    else:
        if opening_brackets:
            current_opening_bracket = opening_brackets.pop()
            if not values[current_opening_bracket] == char:
                balanced = False
                break
        else:
            balanced = False
            break

if balanced:
    print('YES')
else:
    print('NO')