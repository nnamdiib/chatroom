import datetime
import cPickle as pickle
from pprint import pprint
import requests
import anydbm
import sqlite3
import os
import json




url = 'http://127.0.0.1:8000/studentable/json'

payload = {'level': '100', 'major': 'Computer Science', 'semester': 'Alpha'}

#r = requests.get(url, payload)
data = [{"level": "100", "semester": "alpha", "course_code": "csc121", "course_title": "default", "mon": "00:00", "tue": "00:00", "wed": "00:00", "thu": "10 - 12 PM", "fri": "2 - 3 PM", "major": [1, 6]}]

data_string = pickle.dumps(data)


data2 = pickle.loads(data_string)



def create_db(db_filename):
	db_is_new = not os.path.exists(db_filename)
	schema = 'schema.sql'
	with sqlite3.connect(db_filename) as conn:
		if db_is_new:
			print "Creating Database...."
			with open(schema, 'rt') as f:
				schema = f.read()
			print "Creating schema..."
			conn.executescript(schema)
		else:
			print "Database already exists. Assume same for schema."



def insert(obj, db_filename):
	data = json.loads(obj)
	with sqlite3.connect(db_filename) as conn:
		print "Inserting data:"
		room = data['room']
		user = data['username']
		message = data['payload']

		msg_insert = """
		insert into messages (room, username, message)
		values (:room, :user, :message)
		"""
		conn.execute(msg_insert, {'room':room, 'user':user, 'message':message})

	print "data has been inserted. :)"

def get(msg):
	a = []
	d = json.loads(msg)
	a.append(d)
	print a
	
def main():
	print "I have been imported"

if __name__ == "__main__":
	main()

'''
with sqlite3.connect(db_filename) as connection:
	if db_is_new:
		print 'Creating schema'
		with open(schema, 'rt') as f:
			schema = f.read()
		connection.executescript(schema)

		print 'Inserting initial data'
		today = datetime.date.today()
		
		connection.execute("""
		insert into project (name, description, deadline)
		values ('ClamChat', 'A simple service using Tornado for chat groups', '2010-11-01')		
			""")

		connection.execute("""
		insert into task (details, status, deadline, project)
		values ('Create nice UI', 'done', '2010-10-17', 'ClamChat' )
		""")

		connection.execute("""
		insert into task (details, status, deadline, project)
		values ('Message Persistence for chat history.', 'Wating', '2010-10-23', 'ClamChat')
		""")

	else:
		print 'Database Exists, assume schema does as well'

 ## After creating the db, adding a schema and inserting intial data,
 ## Let's query some data from our stuff. 
 ## It is a 2-step process, first you iset he cursor method
 ## then you select_all

with sqlite3.connect(db_filename) as connection:
	cursor = connection.cursor()
	print 'Fetching records...'
	cursor.execute("""
	select id, priority, details, status, deadline from task where project = 'ClamChat'
	""")

	for row in cursor.fetchall():
		## cursor.fetchall() retrieves a tuple. SO unpack it. 
		task_id, priority, details, status, deadline = row
		print row
		#print len(details),
		#print '%-10d {%d} %-40s [%-8s] (%s) ' %(task_id, priority, details, status, deadline)

'''