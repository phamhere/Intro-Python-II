from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber!"""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Room items
room['outside'].items = ['torch', 'key']
room['foyer'].items = ['broken glasses', 'flowers']
room['overlook'].items = ['pendant']
room['narrow'].items = []
room['treasure'].items = ['gold', 'ring']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def describe_room(room):
    print(p.room)
    if p.room.items == []:
        print('This room holds no items.')
    else:
        print(
            f"This room holds {len(p.room.items)} item(s): {', '.join(p.room.items)}.")


i = ''
while i != 'q' and 'gold' not in p.inventory:
    describe_room(p.room)
    print(p)
    print('Move with [n], [s], [e], or [w], pick up items with [get [item]]/[take [item]], drop items with [drop [item]], or quit with [q]!')
    i = input('>> ')

    if len(i.split()) == 1:
        if i == 'n' and hasattr(p.room, 'n_to'):
            p.room = p.room.n_to
        elif i == 's' and hasattr(p.room, 's_to'):
            p.room = p.room.s_to
        elif i == 'e' and hasattr(p.room, 'e_to'):
            p.room = p.room.e_to
        elif i == 'w' and hasattr(p.room, 'w_to'):
            p.room = p.room.w_to
        elif i == 'q':
            pass
        else:
            print('That move isn\'t allowed, please try again.')
    elif len(i.split()) == 2:
        if i.split()[0] == 'get' or i.split()[0] == 'take':
            if i.split()[1] in p.room.items:
                p.inventory.append(i.split()[1])
                p.room.items.remove(i.split()[1])
            else:
                print('That item doesn\'t exist in the room.')
        elif i.split()[0] == 'drop':
            if i.split()[1] in p.inventory:
                p.inventory.remove(i.split()[1])
                p.room.items.append(i.split()[1])
            else:
                print('That item doesn\'t exist in your inventory.')
    else:
        print('That move isn\'t allowed, please try again.')

if 'gold' in p.inventory:
    print('You win! You found the treasure!')
