import hashlib #for hash()
import binascii #for hash()

def encrypt(data, key): #encryption-algorithm, right now uses xor -.- data, key, return :: string
	i = 0
	xored = ''
	for j in data:
		xored += chr(ord(key[i]) ^ ord(j))
		i = (i+1)%len(key)
	return xored

def decrypt(data, key): #see above
	return crypt(data, key)

def hash(data): #ordinary hash function data, return :: string
	h = hashlib.new('sha512')
	h.update(data .encode())
	return binascii.unhexlify(h.hexdigest()).decode('ascii', 'ignore')