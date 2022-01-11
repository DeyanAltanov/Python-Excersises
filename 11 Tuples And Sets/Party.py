reservations_count = int(input())
reservation_guests = set()
arrived_guests = set()

for _ in range(reservations_count):
    reservation_guests.add(input())

command = input()

while command != 'END':
    arrived_guests.add(command)
    command = input()

missing_guests = reservation_guests.difference(arrived_guests)

vip_guests_missing = []
regular_guests_missing = []

for guest in missing_guests:
    if guest[0].isdigit():
        vip_guests_missing.append(guest)
    else:
        regular_guests_missing.append(guest)

print(len(vip_guests_missing) + len(regular_guests_missing))
vip_guests_missing = sorted(vip_guests_missing)
regular_guests_missing = sorted(regular_guests_missing)
for guest in vip_guests_missing:
    print(guest)
for guest in regular_guests_missing:
    print(guest)