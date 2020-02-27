#Albert Wan
#SoftDev pd9
#K09 - Yummy Mongo Py
#2020-02-26

from pymongo import MongoClient
from bson.json_util import loads
client = MongoClient('localhost', 27017)

db1 = client.someDB
db = db1.restaurants

def get_borough(bor):

def get_zip(zip):

def get_zipgrade(zip, grade):

def get_zipthresh(zip, thresh):
