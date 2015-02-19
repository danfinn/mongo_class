#!/usr/bin/python

import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.photos
image_collection = database.images
album_collection = database.albums

image_collection_records=image_collection.find()
album_collection_records=album_collection.find()

album_photo_ids = []
orphans = []
image = ""
for image in album_collection_records:
	for i in image['images']:
		if i not in album_photo_ids:
			album_photo_ids.append(i)

#print album_photo_ids

image = ""
for image in image_collection_records:
	if image['_id'] not in album_photo_ids:
		orphans.append(image['_id'])

#print orphans

image = ""
for image in orphans:
	image_collection.remove({'_id':image})
