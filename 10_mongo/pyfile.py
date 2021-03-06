#Albert Wan, Calvin Chu - Team Short Circuit
#SoftDev1 pd9
#K10: Import/Export Bank
#2020-02-28

#Dataset is called pokedex, and contains pokemon names and features.
#The features of the pokemon include their type, height, weight, candy count,
#spawn chance, multipliers, weaknesses, and evolve names.

#https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json

#
from pymongo import MongoClient
from bson.json_util import loads
import pprint, numbers

client = MongoClient()
collection = db.pokemon
db = client.ShortCircuit

if (collection.count() == 0):
    f = open("pokedex.json","r")
    response = f.read()
    data = loads(response)
    f.close()
    for post in data['pokemon']:
        collection.insert_one(post)

def getID(id):
    for x in (collection.find({"id" : id})):
        pprint.pprint(x)
def getNum(num):
    for x in (collection.find({"num" : num})):
        pprint.pprint(x)
def getName(name):
    for x in (collection.find({"name" : name})):
        pprint.pprint(x)
def getImg(img):
    for x in (collection.find({"img" : img})):
        pprint.pprint(x)
def getType(t):
    for x in (collection.find({"type" : {"$in" : [t]}})):
        pprint.pprint(x)
def getTypes(t1, t2):
    for x in (collection.find({"$and" : [{"type" : {"$in" : [t1]}}, {"type" : {"$in" : [t2]}} ]})):
        pprint.pprint(x)
def getMaxHeight(h):
    h = float(h)
    while (h > 0):
	i = "{:0.2f}".format(h) + " m"
        for x in (collection.find({"height" : i})):
	    pprint.pprint(x)
	h -= .01
def getMaxWeight(w):
    w = float(w)
    while (w > 0):
        i = "{:0.1f}".format(w) + " kg"
        for x in (collection.find({"weight" : i})):
            pprint.pprint(x)
        w -= .1
def getCandy(c):
    for x in (collection.find({"candy" : c})):
        pprint.pprint(x)
def getCandyCount(c):
    for x in (collection.find({"candy_count" : c})):
        pprint.pprint(x)
def getMaxEgg(e):
    if (isinstance(e, numbers.Number)):
        while (e > 0):
            i = str(int(e)) + " km"
            for x in (collection.find({"egg" : i})):
                 pprint.pprint(x)
            e -= 1
    else:
        for x in (collection.find({"egg" : e})):
            pprint.pprint(x)
def getMaxSpawnChance(c):
    for x in (collection.find({"spawn_chance" : {"$lte" : c}})):
        pprint.pprint(x)
def getMaxAvgSpawns(s):
    for x in (collection.find({"avg_spawns" : {"$lte" : s}})):
        pprint.pprint(x)
def getSpawnTime(t):
    for x in (collection.find({"spawn_time" : t})):
        pprint.pprint(x)
def getMultipliers(m):
    for x in (collection.find({"multipliers" : {"$in" : [m]}})):
        pprint.pprint(x)
def getWeakness(w):
    for x in (collection.find({"weaknesses" : {"$in" : [w]}})):
        pprint.pprint(x)
def getNextEvNum(n):
    for x in (collection.find({"next_evolution.num" : n})):
        pprint.pprint(x)
def getNextEvName(n):
    for x in (collection.find({"next_evolution.name" : n})):
        pprint.pprint(x)
def getPrevEvNum(n):
    for x in (collection.find({"prev_evolution.num" : n})):
        pprint.pprint(x)
def getPrevEvName(n):
    for x in (collection.find({"prev_evolution.name" : n})):
        pprint.pprint(x)
