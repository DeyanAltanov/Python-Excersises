rows, cols = [int(el) for el in input().split()]

matrix = [[f'{chr(letter)}{chr(char)}{chr(letter)}' for char in range(letter, letter + cols)] for letter in range(ord('a'), ord('a') + rows)]

print(*[f"{' '.join(row)}" for row in matrix], sep='\n')