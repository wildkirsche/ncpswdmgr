import crypto

class pswdDB():
	def __init__(self, mpswd):
		self.mpswd = crypto.hash(mpswd)
		self.DB = {}

	def copy(self):
		x = pswdDB('')
		x.mpswd = self.mpswd
		x.data = self.x
		return x
