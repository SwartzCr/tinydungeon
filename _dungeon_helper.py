#!/usr/bin/env python3
import random

#basics
wall = u"\u2b1b"
floor = u"\u2b1c"

#food
beer = u"\U0001f37a"
cheese = u"\U0001f9c0"
chocolate = u"\U0001f36b"
fruit = u"\U0001f351"
meat = u"\U0001f356"
mushroom = u"\U0001f344"
pizza = u"\U0001f355"
FOODS = ([beer]*3+
         [cheese]*5+
         [chocolate]*2+
         [fruit]*5+
         [meat]*10+
         [mushroom]*2+
         [pizza]*3)

#items
bag_of_holding = u"\U0001f45d"
book = u"\U0001f4d5"
boots = u"\U0001f462"
bow_arrow = u"\U0001f3f9"
brass_torch = u"\U0001f526"
camera = u"\U0001f4f7"
candle = u"\U0001f56f"
crown = u"\U0001f451"
chest = u"\U0001f381"
credit_card = u"\U0001f4b3"
crossed_swords = u"\u2694"
crystal_ball = u"\U0001f52e"
dagger = u"\U0001f5e1"
gem = u"\U0001f48e"
hat = u"\U0001f3a9"
helmet = u"\u26d1"
horn = u"\U0001f4ef"
key = u"\U0001f5dd"
magic_marker = u"\U0001f58d"
money_bag = u"\U0001f4b0"
pack = u"\U0001f392"
pick_axe = u"\u26cf"
potion = u"\u2697"
prayer_beads = u"\U0001f4ff"
ring = u"\U0001f48d"
scroll = u"\U0001f4dc"
shield = u"\U0001f6e1"
shirt = u"\U0001f455"
shirt2 = u"\U0001f3bd"
ITEMS = ([bag_of_holding]*3+
         [book]*10+
         [boots]*10+
         [bow_arrow]*10+
         [brass_torch]*2+
         [camera]*2+
         [candle]*3+
         [crown]*5+
         [chest]*5+
         [credit_card]*3+
         [crossed_swords]*3+
         [crystal_ball]*2+
         [dagger]*5+
         [gem]*2+
         [hat]*3+
         [helmet]*5+
         [horn]*2+
         [key]*3+
         [magic_marker]*3+
         [money_bag]*10+
         [pack]*2+
         [pick_axe]*5+
         [potion]*3+
         [prayer_beads]*2+
         [ring]*5+
         [scroll]*10+
         [shield]*5+
         [shirt]*2+
         [shirt2]*3)

#monuments
bath = u"\U0001f6c1"
shrine = u"\u26e9"
statue = u"\U0001f5ff"
temple = u"\U0001f3db"
web = u"\U0001f578"
fire = u"\U0001f525"
MONUMENTS = ([bath]*1+
             [fire]*2+
             [statue]*3+
             [temple]*2+
             [shrine]*2+
             [web]*2)

#doors
door = u"\U0001f6aa"
DOORS = [door]

#monsters
ant = u"\U0001f41c"
bee = u"\U0001f41d"
bug = u"\U0001f41b"
croc = u"\U0001f40a"
dragon = u"\U0001f409"
dust_vortex = u"\U0001f32a"
elephant = u"\U0001f418"
ghost = u"\U0001f47b"
imp = u"\U0001f47f"
monkey = u"\U0001f412"
ogre = u"\U0001f479"
ox = u"\U0001f402"
rat = u"\U0001f400"
scorpion = u"\U0001f982"
snake = u"\U0001f40d"
sheep = u"\U0001f40f"
unicorn = u"\U0001f984"
w_buffalo = u"\U0001f403"
MONSTERS = ([ant]*1+
            [bee]*1+
            [bug]*1+
            [croc]*5+
            [dragon]*5+
            [dust_vortex]*1+
            [elephant]*5+
            [ghost]*5+
            [imp]*3+
            [monkey]*2+
            [ogre]*5+
            [ox]*10+
            [rat]*1+
            [scorpion]*5+
            [snake]*10+
            [sheep]*5+
            [unicorn]*5+
            [w_buffalo]*5)
#people
thinking = u"\U0001f914"
worried = u"\U0001f625"
dizzy = u"\U0001f635"
grimace = u"\U0001f62c"
berserk = u"\U0001f621"
PLAYERS = [thinking, worried, dizzy, grimace, berserk]

#pets
egg = u"\U0001f423"
cat = u"\U0001f408"
dog = u"\U0001f415"
horse = u"\U0001f40e"
PETS = ([egg]*3+
        [cat]*9+
        [dog]*7+
        [horse])

basic_dungeon =     [[wall]*13,
                    [wall]+[floor]*11 + [wall],
                    [wall]+[floor]*11 + [wall],
                    [wall]+[floor]*11 + [wall],
                    [wall]+[floor]*11 + [wall],
                    [wall]+[floor]*11 + [wall],
                    [wall]+[floor]*11 + [wall],
                    [wall]+[floor]*11 + [wall],
                    [wall]*13]

DUNGEONS = [basic_dungeon]

MONSTER_CLUSTERS = {bee: 10,
                    rat: 4,
                    ox:  2,
                    w_buffalo: 4,
                    snake: 6,
                    bug: 5,
                    ogre: 6}

path = u"\U0001f3fe"

