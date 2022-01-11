cmd = input()

companies = {}

while cmd != 'End':
    company_and_user = cmd.split(' -> ')
    company = company_and_user[0]
    user = company_and_user[1]
    if company not in companies:
        companies[company] = []
    if user not in companies[company]:
        companies[company].append(user)

    cmd = input()

companies = dict(sorted(companies.items(), key=lambda x: x))

for company in companies:
    print(f"{company}")
    for user in companies[company]:
        print(f"-- {user}")