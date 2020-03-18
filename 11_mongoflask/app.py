
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
    arr = []
    for x in (collection.find({"id" : id})):
        arr.append(x)
    return arr
def getNum(num):
    arr = []
    for x in (collection.find({"num" : num})):
        arr.append(x)

    return arr
def getName(name):
    arr = []
    for x in (collection.find({"name" : name})):
        arr.append(x)

    return arr
def getImg(img):
    arr = []
    for x in (collection.find({"img" : img})):
        arr.append(x)

    return arr
def getType(t):
    arr = []
    for x in (collection.find({"type" : {"$in" : [t]}})):
        arr.append(x)

    return arr
def getCandy(c):
    arr = []
    for x in (collection.find({"candy" : c})):
        arr.append(x)
    return arr
def getCandyCount(c):
    arr = []
    for x in (collection.find({"candy_count" : c})):
        arr.append(x)
    return arr
def getMaxSpawnChance(c):
    arr= []
    for x in (collection.find({"spawn_chance" : {"$lte" : c}})):
        arr.append(x)
    return arr
def getMaxAvgSpawns(s):
    arr=[]
    for x in (collection.find({"avg_spawns" : {"$lte" : s}})):
        arr.append(x)
    return arr
def getSpawnTime(t):
    arr=[]
    for x in (collection.find({"spawn_time" : t})):
        arr.append(x)

    return arr
def getMultipliers(m):
    arr=[]
    for x in (collection.find({"multipliers" : {"$in" : [m]}})):
        arr.append(x)
    return arr
def getWeakness(w):
    arr=[]
    for x in (collection.find({"weaknesses" : {"$in" : [w]}})):
        arr.append(x)
    return arr
def getNextEvNum(n):
    arr=[]
    for x in (collection.find({"next_evolution.num" : n})):
        arr.append(x)
    return arr
def getNextEvName(n):
    arr=[]
    for x in (collection.find({"next_evolution.name" : n})):
        arr.append(x)
    return arr
def getPrevEvNum(n):
    arr=[]
    for x in (collection.find({"prev_evolution.num" : n})):
        arr.append(x)
    return arr
def getPrevEvName(n):
    arr=[]
    for x in (collection.find({"prev_evolution.name" : n})):
        arr.append(x)
    return arr


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
