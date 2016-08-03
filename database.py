import datetime
import sqlite3
import os
import json

## User should be able to query the db and get previus messages in current chatroom.

# Should be called only when no DB exists. 
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


# Inserting each sent message into one lump table. 
# Each record should have Message, User (Person that sent it), Room (room message was sent in)
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

# Get method for getting records from the DB 
def get(query, db_filename):
	pass
	
def main():
	print "I have been imported"



if __name__ == "__main__":
	main()
