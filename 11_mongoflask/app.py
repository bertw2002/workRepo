
#Albert Wan (same pokedex file as calvin chu)
#SoftDev1 pd9
#K11: Ay Mon Go Git It From Yer Flask
#2020-03-09


from flask import Flask, render_template, request, redirect, url_for
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
        return x
def getNum(num):
    for x in (collection.find({"num" : num})):
        return x
def getName(name):
    for x in (collection.find({"name" : name})):
        return x
def getImg(img):
    for x in (collection.find({"img" : img})):
        return x
def getType(t):
    for x in (collection.find({"type" : {"$in" : [t]}})):
        return x
def getTypes(t1, t2):
    for x in (collection.find({"$and" : [{"type" : {"$in" : [t1]}}, {"type" : {"$in" : [t2]}} ]})):
        return x
def getCandy(c):
    for x in (collection.find({"candy" : c})):
        return x
def getCandyCount(c):
    for x in (collection.find({"candy_count" : c})):
        return x
def getMaxSpawnChance(c):
    for x in (collection.find({"spawn_chance" : {"$lte" : c}})):
        return x
def getMaxAvgSpawns(s):
    for x in (collection.find({"avg_spawns" : {"$lte" : s}})):
        return x
def getSpawnTime(t):
    for x in (collection.find({"spawn_time" : t})):
        return x
def getMultipliers(m):
    for x in (collection.find({"multipliers" : {"$in" : [m]}})):
        return x
def getWeakness(w):
    for x in (collection.find({"weaknesses" : {"$in" : [w]}})):
        return x
def getNextEvNum(n):
    for x in (collection.find({"next_evolution.num" : n})):
        return x
def getNextEvName(n):
    for x in (collection.find({"next_evolution.name" : n})):
        return x
def getPrevEvNum(n):
    for x in (collection.find({"prev_evolution.num" : n})):
        return x
def getPrevEvName(n):
    for x in (collection.find({"prev_evolution.name" : n})):
        return x


app = Flask(__name__)

@app.route("/")
def root():
    if (len(request.args) == 0 ):
        return render_template('poke.html')
    if (len(request.args['input']) == 0):
        return render_template('poke.html')
    else:
        if (request.args['search'] == 'id'):
            return render_template('app.html', var = getID(int(request.args['input'])))
        if (request.args['search'] == 'num'):
            return render_template('app.html', var = getNum(request.args['input']))
        if (request.args['search'] == 'name'):
            return render_template('app.html', var = getName(request.args['input']))
        if (request.args['search'] == 'img'):
            return render_template('app.html', var = getImg(request.args['input']))
        if (request.args['search'] == 'type'):
            return render_template('app.html', var = getType(request.args['input']))
        if (request.args['search'] == 'candy'):
            return render_template('app.html', var = getCandy(request.args['input']))
        elif (request.args['search'] == 'weakness'):
            return render_template('app.html', var = getWeakness(request.args['input']))

if __name__ == "__main__":
    app.debug = True
    app.run()
