def draw_rhombus(size):
    count = 1
    for index in range(size):
        print(f"{(size - index - 1) * ' '}{count * '* '}")
        count += 1
    count = size - 1
    for index in range(size - 2, -1, -1):
        print(f"{(size - index - 1) * ' '}{count * '* '}")
        count -= 1


draw_rhombus(int(input()))