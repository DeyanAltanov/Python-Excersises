text = input()

vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']

no_vowels = ''.join([char for char in text if char not in vowels])

print(no_vowels)