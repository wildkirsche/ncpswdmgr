def encrypt(data, key): #encryption-algorithm, right now simple xor -.- data, key, return :: string
	i = 0
	xored = ''
	for j in data:
		xored += chr(ord(key[i]) ^ ord(j))
		i = (i++)%len(key)
	return xored

def decrypt(data, key): #see above
	return crypt(data, key)
