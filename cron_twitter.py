from twython import Twython
import json
import random
import dungeon

def auth():
    with open("access.json", 'r') as f:
        db = json.load(f)
    return Twython(db["API_Key"], db["API_Secret"], db["Access_Token"], db["Access_Token_Secret"])

def do_thing():
    twitter = auth()
    tweet = dungeon.gen_dungeon()
    twitter.update_status(status=tweet)


do_thing()
