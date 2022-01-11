def combinations(names, chairs, all_combinations=[]):
    if len(all_combinations) == chairs:
        print(", ".join(all_combinations))
        return

    for index in range(len(names)):
        name = names[index]
        all_combinations.append(name)
        combinations(names[index + 1:], chairs, all_combinations)
        all_combinations.pop()


names = input().split(', ')
chairs = int(input())

combinations(names, chairs)