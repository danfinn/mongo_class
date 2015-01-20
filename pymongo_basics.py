from pymongo import MongoClient

# connect to hw1 collection of m101 mongo db
client=MongoClient()
db=client.m101
collection=db.hw1

# find first entry
print collection.find_one()

# print all entries
for doc in collection.find():
    print doc
