all_electrons = int(input())
current_electrons = all_electrons

shells = []
shell = 0

while not current_electrons <= 0:

    shell_value = 2 * pow(shell + 1, 2)
    if current_electrons >= shell_value:
        shells.append(shell_value)
    else:
        shells.append(current_electrons)
    current_electrons -= shell_value
    shell += 1

print(shells)