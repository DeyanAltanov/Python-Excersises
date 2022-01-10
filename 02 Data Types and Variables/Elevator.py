people = int(input())
capacity = int(input())
courses = 0

while people > 0:
    if people - capacity >= 0:
        people -= capacity
        courses += 1
    else:
        courses += 1
        people = 0

print(courses)