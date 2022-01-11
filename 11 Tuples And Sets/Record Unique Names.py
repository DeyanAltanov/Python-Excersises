name_count = int(input())

unique_names = set()

for _ in range(name_count):
    unique_names.add(input())

for name in unique_names:
    print(name)