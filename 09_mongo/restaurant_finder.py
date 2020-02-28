#Albert Wan
#SoftDev pd9
#K09 - Yummy Mongo Py
#2020-02-26

from pymongo import MongoClient
from bson.json_util import loads
client = MongoClient('localhost', 27017)

db1 = client.restaurants
db1.databse.drop()
db = db1.databse

with open("primer-dataset.json", "r") as file:
  data = file.readlines()
  for x in data:
    db.insert_one(loads(data))

def get_borough(bor):
    val = db.find({ "borough": bor})
    for x in val:
        print(x["name"])
#get_borough("Brooklyn")


def get_zip(zip):
    val = db.find({"address.zipcode": zip})
    for x in val:
        print(x["name"])

def get_zipgrade(zip, grade):
    val = db.find({ "address.zipcode": zip, "grades.grade": grade })
    for x in val:
        print(x["name"])

def get_zipthresh(zip, thresh):
    val = db.find({"address.zipcode": zip, "grades.score": { "$lt": thresh }})
    for x in val:
        print(x["name"])
