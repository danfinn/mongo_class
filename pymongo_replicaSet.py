#!/usr/bin/python
import pymongo
import sys

c = pymongo.MongoClient(host="mongodb://localhost:27017",replicaSet="m101",w=1,j=True)

db = c.m101
people = db.people

try:
   print "inserting"
   people.insert({"name":"Dan Finn","favorite_color":"red"})
   print "inserting"
   people.insert({"name":"Candice Welch","favorite_color":"blue"})
   print "inserting"
   people.insert({"name":"D Dog","favorite_color":"fish scale"})
except:
   print "Unexpected error:",sys.exc_info()[0]
print "completed the inserts"
