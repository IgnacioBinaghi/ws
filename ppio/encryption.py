import cryptocode

def encrypt(str):
	with open('secret.txt') as f:
		secret = f.read()
	encrypted = cryptocode.encrypt(str, secret)
	return encrypted

def decrypt(str):
	with open('secret.txt') as f:
		secret = f.read()
	decrypted = cryptocode.decrypt(str, secret)
	return decrypted