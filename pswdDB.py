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