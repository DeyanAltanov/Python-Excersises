employees_happiness = input().split()
factor = int(input())

happiness = [int(employee) for employee in employees_happiness]

increased_happiness = []

for employee in happiness:
    increased_happiness.append(employee * factor)

average = sum(increased_happiness) / len(increased_happiness)

filtered = [employee for employee in increased_happiness if employee >= average]

if len(filtered) < len(increased_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(increased_happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(filtered)}/{len(increased_happiness)}. Employees are happy!")