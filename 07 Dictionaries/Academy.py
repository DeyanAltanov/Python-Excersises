pairs = int(input())

all_students = {}
good_students = {}

for student in range(0, pairs):
    name = input()
    grade = float(input())

    if name not in all_students:
        all_students[name] = []
    all_students[name].append(grade)

for student in all_students:
    average = sum(all_students[student]) / len(all_students[student])
    if average >= 4.50:
        good_students[student] = f"{average:.2f}"

good_students = sorted(good_students.items(), key=lambda x: x[1], reverse=True)

for student, grade in good_students:
    print(f"{student} -> {grade}")