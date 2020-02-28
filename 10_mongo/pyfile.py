#Albert Wan, Calvin Chu, Team Short Circuit
#SoftDev pd9
#K10: Import/Export Bank
#2020-02-28

from pymongo import MongoClient
from bson.json_util import loads
import pprint
client = MongoClient('localhost', 27017)
db = client.test
collection = db.restaurants
if (not "restaurants" in db.list_collection_names()):
    f = open("data.json","r")
    response = f.read()
    data = loads(response)
    f.close()
    for post in data:
        collection.insert_one(post)
