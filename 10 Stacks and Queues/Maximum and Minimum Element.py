queries = int(input())
stack = []

for q in range(queries):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        if len(stack) > 0:
            stack.pop()
    elif query[0] == 3:
        if len(stack) > 0:
            print(max(stack))
    elif query[0] == 4:
        if len(stack) > 0:
            print(min(stack))

final_stack = []

for number in range(0, len(stack)):
    digit = stack.pop()
    final_stack.append(str(digit))

print(', '.join(final_stack))