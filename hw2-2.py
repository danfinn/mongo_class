import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

db=connection.students
scores = db.grades


def find():
    seen_student={}

    print "find, reporting for duty"

    query = {'type':'homework'}

    try:

        cursor = scores.find(query)
       # cursor = cursor.limit(1)

        
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in cursor:
	student_id=doc['student_id']
	#print student_id
        if not student_id in seen_student:
		seen_student[student_id] = 1
	else:
		scores.remove(doc)
		#print doc
find()
