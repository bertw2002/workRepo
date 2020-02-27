#Albert Wan
#SoftDev pd9
#K09 - Yummy Mongo Py
#2020-02-26

from pymongo import MongoClient
from bson.json_util import loads
client = MongoClient('localhost')

db = client.restaurants
