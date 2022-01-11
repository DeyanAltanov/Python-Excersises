class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
                self.guests += people
                break

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()
                break

    def print_status(self):
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join([str(room) for room in self.rooms if not room.is_taken])}")
        print(f"Taken rooms: {', '.join([str(room) for room in self.rooms if room.is_taken])}")