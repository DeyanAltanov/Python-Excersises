number = int(input())
longest_intersection = set()

for _ in range(number):
    ranges = input().split('-')
    first_range = list(map(int, ranges[0].split(',')))
    second_range = list(map(int, ranges[1].split(',')))
    first_set = set()
    second_set = set()
    for i in range(first_range[0], first_range[-1] + 1):
        first_set.add(i)
    for i in range(second_range[0], second_range[-1] + 1):
        second_set.add(i)
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(map(lambda number: str(number), longest_intersection))}] with length {len(longest_intersection)}")