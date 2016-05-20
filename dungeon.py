import random
import _dungeon_helper

#DOORS = _dungeon_helper.DOORS
DUNGEONS = _dungeon_helper.DUNGEONS
MONSTERS = _dungeon_helper.MONSTERS
MONSTER_CLUSTERS = _dungeon_helper.MONSTER_CLUSTERS
ITEMS = _dungeon_helper.ITEMS
FOODS = _dungeon_helper.FOODS
MONUMENTS = _dungeon_helper.MONUMENTS
PLAYERS = _dungeon_helper.PLAYERS
PETS = _dungeon_helper.PETS
floor = _dungeon_helper.floor
wall = _dungeon_helper.wall

room_tries = 40
action_tries = 16
width, height = (13,10)

def gen_dungeon_border(rooms):
    out = []
    for y in range(height):
        for x in range(width):
            if y == 0 or y == height-1:
                out.append((x,y))
            elif x == 0 or x == width -1:
                out.append((x,y))
    out = set(out).difference(rooms)
    return list(out)

def get_width_height(dungeon):
    return (len(dungeon[0]), len(dungeon))

def get_random_x_y(dungeon, rooms):
    return random.choice(list(rooms))

def draw(places, tile, dungeon):
    for space in places:
        x, y = space
        dungeon[y][x] = tile

def gen_dungeon():
#    TEMPLATE_DUNGEON = random.choice(DUNGEONS)
    dungeon, empty_spaces = make_dungeon_outline()
    rooms, room_list = gen_rooms(empty_spaces)
    paths = gen_paths(room_list)
    draw(list(rooms), _dungeon_helper.floor, dungeon)
    draw(list(paths), _dungeon_helper.path, dungeon)
    rooms = rooms.union(paths)
    decorate_room(dungeon, rooms)
#    dungeon = _dungeon_helper.test_dungeon
    printable_dungeon = format_dungeon(dungeon)
    return(printable_dungeon)

def gen_rooms(empty_spaces):
    rooms = set()
    borders = set()
    room_list = []
    for i in range(room_tries):
        potential_room, border, empty_spaces = make_room(empty_spaces)
        if rooms.isdisjoint(potential_room) and borders.isdisjoint(potential_room):
            rooms = rooms.union(potential_room)
            borders = borders.union(border)
            room_list.append(list(potential_room))
    return rooms, room_list

def gen_paths(room_list):
    paths = set()
    coords = sorted([[min(room), max(room)] for room in room_list])
    for idx,room1 in enumerate(coords):
        for room2 in coords[idx+1:]:
            x_overlap = sorted(list(set(range(room1[0][0],room1[1][0]+1)).intersection(set(range(room2[0][0], room2[1][0]+1)))))
            y_overlap = sorted(list(set(range(room1[0][1],room1[1][1]+1)).intersection(set(range(room2[0][1], room2[1][1]+1)))))
            if len(x_overlap):
                ys = sorted([room1[0][1], room1[1][1], room2[0][1], room2[1][1]])
                y_difference = sorted(list(set(range(ys[1]+1, ys[2]))))

                #y_difference = sorted(list(set(range(min([room1[1][1], room2[0][1]])+1,
                #                                     max([room1[1][1], room2[0][1]])))))
                path = make_v_path(x_overlap, y_difference)
                paths = paths.union(path)
            elif len(y_overlap):
                xs = sorted([room1[0][0], room1[1][0], room2[0][0], room2[1][0]])
                x_difference = sorted(list(set(range(xs[1]+1, xs[2]))))
                #x_difference = sorted(list(set(range(min([room1[1][0], room2[0][0]])+1,
                #                                     max([room1[1][0], room2[0][0]])))))
                path = make_h_path(x_difference, y_overlap)
                paths = paths.union(path)
                continue
    return paths

def make_v_path(x, y):
    path = set()
    if len(y) == 1:
        path.add((random.choice(x), y[0]))
        return path
    x1 = random.choice(x)
    y1 = y[0]
    path.add((x1, y1))
    y1 += 1
    path.add((x1, y1))
    xendpoint = random.choice([x[0], x[-1]])
    if xendpoint > x1:
        direction = 1
    else:
        direction = -1
    while y1 != y[-1]:
        if x1 != xendpoint and random.choice([0,1]):
            x1 += direction
            path.add((x1, y1))
        else:
            y1 += 1
            path.add((x1, y1))
    return path

def make_h_path(x, y):
    path = set()
    if len(x) == 1:
        path.add((x[0], random.choice(y)))
        return path
    x1 = x[0]
    y1 = random.choice(y)
    path.add((x1, y1))
    x1 += 1
    path.add((x1,y1))
    yendpoint = random.choice([y[0], y[-1]])
    if yendpoint > y1:
        direction = 1
    else:
        direction = -1
    while x1 != x[-1]:
        if y1 != yendpoint and random.choice([0,1]):
            y1 += direction
            path.add((x1, y1))
        else:
            x1 += 1
            path.add((x1, y1))
    return path
    return path

def make_dungeon_outline():
    empty_spaces = set()
    for i in range(10):
        for j in range(13):
            empty_spaces.add((j,i))
    return [[_dungeon_helper.wall]*13 for i in range(10)], empty_spaces

def make_room(empty_spaces):
    startx = random.randint(0,11)
    starty = random.randint(0,8)
    x = random.randint(2,8)
    y = random.randint(2,8)
    room = set()
    border = set()
    for i in range(y):
        for j in range(x):
            if i == 0:
                if 0 < (starty-1):
                    border.add((min([startx+j, width-1]), starty-1))
            elif i == y-1:
                if i+starty < height:
                    border.add((min([startx+j, width-1]), starty+i+1))
            if j == 0:
                if 0 < (startx-1):
                    border.add((startx-1, min([starty+i, height-1])))
            elif j == x-1:
                if j+startx < width:
                    border.add((startx+j+1, min([starty+i, height-1])))
            room.add((min([startx+j, width-1]),min([starty+i,height-1])))
    empty_spaces = empty_spaces.difference(room)
    return room, border, empty_spaces

def decorate_room(dungeon, rooms):
    x, y = add_player(dungeon, rooms)
    for i in range(action_tries):
        action = ACTIONS.pop(random.randint(0, len(ACTIONS)-1))
        action(dungeon, rooms)

def add_player(dungeon, rooms):
    player = random.choice(PLAYERS)
    x, y = get_random_x_y(dungeon, rooms)
    dungeon[y][x] = player
    return (x, y)

def add_pet(dungeon, x, y):
    x = x + random.randint(-1,1)
    y = y + random.randint(-1,1)
    if dungeon[y][x] == floor:
        dungeon[y][x] = random.choice(PETS)

#def add_door(dungeon):
#    door = random.choice(DOORS)
#    width, height = get_width_height(dungeon)
#    pos_doors = (width*2) + ((height-2)*2)
#    placement = random.randint(0, pos_doors)
#    if placement < width:
#        dungeon[0][placement] = door
#    elif placement > pos_doors-width:
#        dungeon[-1][placement-(pos_doors - width)] = door
#    else:
#        dungeon[int((placement-13)/2)][-(placement%2)] = door #ewww

def place_monster(dungeon, rooms):
    x, y = get_random_x_y(dungeon, rooms)
    if dungeon[y][x] == floor:
        monster = random.choice(MONSTERS)
        if monster:
            dungeon[y][x] = monster

def place_monster_cluster(dungeon, rooms):
    width, height = get_width_height(dungeon)
    x, y = get_random_x_y(dungeon, rooms)
    monster = random.choice(list(MONSTER_CLUSTERS.keys()))
    for i in range(MONSTER_CLUSTERS[monster]):
        if 0 < x < width and 0 < y < height and dungeon[y][x] == floor:
            dungeon[y][x] = monster
            y += random.randint(-1,1)
            x += random.randint(-1,1)


def place_food(dungeon, rooms):
    x, y = get_random_x_y(dungeon, rooms)
    if dungeon[y][x] == floor:
        food = random.choice(FOODS)
        if food:
            dungeon[y][x] = food

def place_item(dungeon, rooms):
    x, y = get_random_x_y(dungeon, rooms)
    if dungeon[y][x] == floor:
        item = random.choice(ITEMS)
        if item:
            dungeon[y][x] = item

def place_monument(dungeon, rooms):
    x, y = get_random_x_y(dungeon, rooms)
    if dungeon[y][x] == floor:
        monument = random.choice(MONUMENTS)
        if monument:
            dungeon[y][x] = monument

def format_dungeon(dungeon):
    return "\n".join(["".join(row) for row in dungeon])

def do_nothing(a, b):
    return

ACTIONS = ([place_monster]*10+
           [place_monster_cluster]*2+
           [place_item]*5+
           [place_food]*3+
           [place_monument]*2+
           [do_nothing]*5)
