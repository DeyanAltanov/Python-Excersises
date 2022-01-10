lines = int(input())
balanced = ""
brackets = "BALANCED"

for i in range(0, lines):
    char = input()
    if char == '(' or char == ')':
        balanced += char

if balanced[0] == ')':
    brackets = "UNBALANCED"
else:
    for i in range(0, len(balanced)):
        if i + 1 <= len(balanced) - 1:
            if balanced[i] == '(':
                if balanced[i + 1] == '(':
                    brackets = "UNBALANCED"
                    break
            elif balanced[i] == ')':
                if balanced[i + 1] == ')':
                    brackets = "UNBALANCED"
                    break

print(brackets)