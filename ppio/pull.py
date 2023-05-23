
# Controlls all pull functions in the database
from .basic import *
from .encryption import *

def login(username, password):
	user = get_collection().find_one({"user": username})
	if (user == None):
		return False
	if (decrypt(user["pass"]) != password):	
		return False
	else:
		with open("resources/id.txt", "w") as w:
			w.write(user["_id"])
		return True

def get_user(id):
	return get_collection().find_one({"_id": id})