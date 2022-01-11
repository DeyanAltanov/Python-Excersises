names_count = int(input())

students = {}

for student_grade in range(names_count):
    name_grade = input().split()
    name = name_grade[0]
    grade = float(name_grade[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    print(f"{student} -> {grades_string} (avg: {(sum(grades) / len(grades)):.2f})")