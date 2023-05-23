""" 
Controls all push functions to the database
Isaac
"""
from pymongo import MongoClient
from .basic import get_collection
import certifi
import time
from get_user_data import get_user_info
from encryption import decrypt

def current_user():
	# Returns id of the current user from resources/id.txt
	with open("resources/id.txt", "r") as r:
		return r.readline()

def push_to_db(user):
	# Pushes the user to the database with a unique id
	user["_id"] = str(time.time())
	get_collection().insert_one(user)
	# This is a relative path and may cause issues later
	with open("resources/id.txt", "w") as w:
		w.write(user["_id"])
	return user

def update_email(query, email):
	# Pushes the courses to the currents users course string
	newvalue = {"$set": {"email": email}}
	get_collection().update_one(query, newvalue)

def update_keyword1(query, keyword1):
	# Pushes the courses to the currents users course string
	newvalue = {"$set": {"keyword1": keyword1}}
	get_collection().update_one(query, newvalue)

def update_keyword2(query, keyword2):
	# Pushes the topics to the current user's topics string
	newvalue = {"$set": {"keyword2": keyword2}}
	get_collection().update_one(query, newvalue)

def update_keyword3(query, keyword3):
	# Pushes the area to the given user's area string
	newvalue = {"$set": {"keyword3": keyword3}}
	get_collection().update_one(query, newvalue)

def update_keyword4(query, keyword4):
	# Pushes the bio to the given user's bio string
	newvalue = {"$set": {"keyword4": keyword4}}
	get_collection().update_one(query, newvalue)

def update_keyword5(query, keyword5):
	# Pushes the bio to the given user's bio string
	newvalue = {"$set": {"keyword5": keyword5}}
	get_collection().update_one(query, newvalue)


def push_to_db_repeat(user):
	info = get_user_info()
	for i in info:
		if decrypt(user['email']) == decrypt(i[1][5:]):
			identity = {"_id": i[0]}
			break
	print(user)
	update_keyword1(identity, user['keyword1'])
	update_keyword2(identity, user['keyword2'])
	update_keyword3(identity, user['keyword3'])
	update_keyword4(identity, user['keyword4'])
	update_keyword5(identity, user['keyword5'])

