import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

db=connection.school
scores = db.students


def find():
    seen_student={}

    print "find, reporting for duty"

    query = {}

    try:

        cursor = scores.find(query)
       # cursor = cursor.limit(1)

        
        #cursor = cursor.sort([('_id',pymongo.ASCENDING),('scores',pymongo.DESCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in cursor:
	student_id=doc['_id']
	score1=doc["scores"][2]["score"]
        score2=doc["scores"][3]["score"]
        print student_id	
	if (float(score1) < float(score2)):
	   print "%s is the lowest score" %score1
           scores.update({"_id":student_id},{"$pull":{"scores":{"type":"homework","score":score1}}})
	else:
	   print "%s is the lowest score" %score2
 	   scores.update({"_id":student_id},{"$pull":{"scores":{"type":"homework","score":score2}}})
        #if not student_id in seen_student:
	#	seen_student[student_id] = 1
	#else:
	#	scores.remove(doc)
	#	#print doc
find()
