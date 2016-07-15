import datetime
import datetime
import cPickle as pickle
from pprint import pprint
import requests
import anydbm
import sqlite3
import os
import json


with sqlite3.connect('clamchat.db') as conn:

	cursor = conn.cursor()
	cursor.execute("""
	select room, username, message from messages
	""")
	for row in cursor.fetchall():
		room, username, message = row
		print '(%-10s) in {%-10s} said [%s]' % (username, room, message)