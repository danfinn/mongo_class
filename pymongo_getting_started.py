import pymongo

from pymongo import MongoClient

#connect to Mongo
connection = MongoClient('localhost',27017)

# use test DB
db = connection.names

# use names colllection
names = db.names

item = names.find_one()

print item['name']
