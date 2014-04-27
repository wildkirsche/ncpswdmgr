import crypto
import pickle

class pswdDB():
	def __init__(self, mpswd):
		self.mpswd = crypto.hash(mpswd)
		self.DB = {}

	def copy(self):
		x = pswdDB('')
		x.mpswd = self.mpswd
		x.DB = self.DB
		return x

def loadDB(path):
	x = pswdDB('')
	x.DB, x.mpswd = pickle.load(open(path, "rb"))
	return x

def saveDB(path, DB):
	pickle.dump((DB.DB, DB.mpswd), open(path, "wb"))

def addpswd(DB, site, login, pswd, mpswd):
	if crypto.hash(mpswd) = DB.mpswd:
		DB.DB[site] = (login, crypto.encrypt(pswd, mpswd))
		return "WIN"
	else:
		return "FAIL"

def getpswd(DB, site, mpswd):
	if crypto.hash(mpswd) = DB.mpswd:
		login , pswd = DB.DB[site]
		return (login, crypto.decrypt(pswd, mpswd))
	else:
		return "FAIL"