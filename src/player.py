# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, inventory=[]):
        self.room = room
        self.inventory = inventory

    def __str__(self):
        return f"Current inventory: {', '.join(self.inventory)}\n"
