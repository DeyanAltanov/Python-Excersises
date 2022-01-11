expression = input()

stack = []

for i in range(len(expression)):
    char = expression[i]
    if char == '(':
        stack.append(i)
    elif char == ')':
        latest_opening_bracket = stack.pop()
        first_closed_bracket = i
        print(f"{expression[latest_opening_bracket:first_closed_bracket]})")