import random


dimensions = (14, 10)
rooms = []
room_tries = 8
corridor_tries = 4
floor = "."
wall == "x"
treasure = [0]*85 + ["$"]*10 + ["*"]*5 + 
monsters = [0]*50 + ["a", "b", "c", "d", "e"]*10
types = [treasure, monsters]

def gen_dungeon():
    dungeon = [[" "]*dimensions[0] for dimension in range(dimensions[1])]
    for i in range(room_tries):
        dungeon = add_room(dungeon)
    if len(rooms) > 1:
        for i in range(corridor_tries):
            dungeon = add_corridor(dungeon)
    return dungeon

def add_room(dungeon):
    width = random.randint(4, dimensions[0]-1)
    height = random.randing(4, dimensions[1]-1))
    x = (dimensions[0] - room_size[0]) - 1
    y = (dimensions[1] - room_size[1]) - 1
    room = (x, y, width, height)
    dungeon, success = try_to_add_room(dungeon, room)
    if success:
        rooms.append(room)
        decorate_room(dungeon, room)

def try_to_add_room(in_dungeon, room):
    x, y, width, height = room
    out_dungeon = in_dungeon[:]
    for i in range(height):
        tile = floor
        if i == 0 or i == height-1:
            tile = wall
        for j in range(width):
            if tile != wall and (j == 0 or j == width-1):
                tile = wall
            else:
                tile = floor
            pos_x = x+j
            pos_y = y+i
            if out_dungeon[pos_y][pos_x] != " ":
                break
            out_dungeon[pos_y][pos_x] = tile
        else:
            return (in_dungeon, False)
    return (out_dungeon, True)

def decorate_room(dungeon, room):
    x, y, width, height = room
    for i in range(1, height-1):
        for j in range(1, width-1):
            obj = random_obj()
            if obj != 0:
                dungeon[y+j][x+i] = obj


def random_obj():
    rand_type = types[random.randint(0, len(types)-1)]
    return rand_type[random.randint(0, 99)]
