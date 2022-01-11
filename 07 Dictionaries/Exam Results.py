command = input()
points = 0

users = {}
submissions = {}

while not command == 'exam finished':
    statistics = command.split('-')
    user = statistics[0]
    language = statistics[1]
    if len(statistics) == 3:
        points = int(statistics[2])
    if user not in users:
        users[user] = points
    if points > users[user]:
        users[user] = points
    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1
    if statistics[1] == 'banned':
        users.pop(user)

    command = input()

users = dict(sorted(users.items(), key=lambda x: x))
users = sorted(users.items(), key=lambda x: x[1], reverse=True)
submissions = dict(sorted(submissions.items(), key=lambda x: x))
submissions = sorted(submissions.items(), key=lambda x: x[1], reverse=True)

print("Results:")
for user, points in users:
    print(f"{user} | {points}")
print("Submissions:")
for language, count in submissions:
    if language != 'banned':
        print(f"{language} - {count}")