class Guest:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end


class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.guests = []

    def is_free(self, start, end):
        for g in self.guests:
            if not (end <= g.start or start >= g.end):
                return False
        return True

    def add_guest(self, guest):
        if self.is_free(guest.start, guest.end):
            self.guests.append(guest)
            return True
        return False


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def free_rooms(self, day):
        count = 0
        for r in self.rooms:
            if r.is_free(day, day+1):
                count += 1
        return count

    def check_in(self, guest):
        for r in self.rooms:
            if r.add_guest(guest):
                print(guest.name, "in room", r.number)
                return
        print("no free room")

    def profit(self):
        total = 0
        for r in self.rooms:
            for g in r.guests:
                days = g.end - g.start
                total += days * r.price
        return total

    def find_guest(self, name):
        for r in self.rooms:
            for g in r.guests:
                if g.name == name:
                    return r.number
        return None

hotel = Hotel()
hotel.add_room(Room(101, 50))
hotel.add_room(Room(102, 40))
g1 = Guest("Anna", 1, 4)
g2 = Guest("Mark", 2, 5)
hotel.check_in(g1)
hotel.check_in(g2)
print("free rooms day 2:", hotel.free_rooms(2))
print("profit:", hotel.profit())
print("Anna room:", hotel.find_guest("Anna"))