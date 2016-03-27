#!/usr/bin/env python3
import random


dimensions = (14, 10)
floor = "◽"
wall = "◼"
basic_dungeon =     [[wall]*14,
                    [wall]+[floor]*12 + [wall],
                    [wall]+[floor]*12 + [wall],
                    [wall]+[floor]*12 + [wall],
                    [wall]+[floor]*12 + [wall],
                    [wall]+[floor]*12 + [wall],
                    [wall]*14]

DUNGEONS = [basic_dungeon]
MONSTERS = [""]*50+["A"]*30+["B"]*20
ITEMS = [""]*50+["/"]*20+["$"]*20+["*"]*10
OBJECTS = [""]*50+["#"]*20+["_"]*30
THINGS = [MONSTERS, ITEMS, OBJECTS]
PLAYERS = ["@"]

item_tries = 10
DOORS = ["+"]

def gen_dungeon():
    TEMPLATE_DUNGEON = random.choice(DUNGEONS)
    dungeon = TEMPLATE_DUNGEON
    decorate_room(dungeon)
    #printable_dungeon = format_dungeon(dungeon)
    printable_dungeon = dungeon
    return(printable_dungeon)

def decorate_room(dungeon):
    width, height = (len(dungeon[0]), len(dungeon))
    add_doors(dungeon, random.randint(0,3))
    add_player(dungeon)
    add_things(dungeon, item_tries)

def add_doors(dungeon, num_doors):
    door = random.choice(DOORS)
    for i in range(num_doors):
        placement = random.randint(0,37)
        if placement < 14:
            dungeon[0][placement] = door
        elif placement > 23:
            dungeon[6][placement-24] = door
        else:
            dungeon[int((placement-14)/2)][-(placement%2)] = door #ewww

def add_player(dungeon):
    width, height = (len(dungeon[0]), len(dungeon))
    player = random.choice(PLAYERS)
    x = random.randint(1, width-2)
    y = random.randint(1, height-2)
    dungeon[y][x] = player

def add_things(dungeon, item_tries):
    width, height = (len(dungeon[0]), len(dungeon))
    for i in range(item_tries):
        x = random.randint(1, width-2)
        y = random.randint(1, height-2)
        if dungeon[y][x] == floor:
            thing = random.choice(random.choice(THINGS))
            if thing:
                dungeon[y][x] = thing

def format_dungeon(dungeon):
    return "\n".join(["".join(row) for row in dungeon])

def random_obj():
    rand_type = types[random.randint(0, len(types)-1)]
    return rand_type[random.randint(0, 99)]
