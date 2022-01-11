course_and_student = input()

courses = {}

while course_and_student != 'end':
    info = course_and_student.split(' : ')
    course = info[0]
    student = info[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    course_and_student = input()

courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for course in courses:
    print(f"{course}: {len(courses[course])}")
    courses[course].sort()
    for student in courses[course]:
        print(f"-- {student}")