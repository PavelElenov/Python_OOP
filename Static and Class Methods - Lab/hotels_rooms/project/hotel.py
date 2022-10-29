class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if not room.is_taken:
                    if room.capacity >= people:
                        self.guests += people
                        room.guests += people
                        room.is_taken = True

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    room.is_taken = False
                    self.guests -= room.guests
                    room.guests = 0

    def status(self):
        ll = [f'Hotel {self.name} has {self.guests} total guests']
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        ll.append(f'Free rooms: {", ".join(str(x) for x in free_rooms)}')
        ll.append(f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}")
        return '\n'.join(ll)
