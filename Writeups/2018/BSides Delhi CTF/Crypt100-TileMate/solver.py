#!/usr/bin/env python2
import string, itertools

from itertools import cycle as scooter
from hashlib import sha384

flag = "flag{"

characters = '0123456789abcdef'
encrypted = open('ci.pher.text','rb').read()

def iter_all_strings():
	length = 2
	while True:
		for s in itertools.product(characters, repeat=length):
			yield "".join(s)
		return

def drive(Helmet, Petrol):
    return ''.join(chr(ord(David)^ord(Toni)) for David,Toni in zip(Helmet,scooter(Petrol)))

def enc(key, flag):
	f = lambda x: sha384(x).digest()[(ord(x)+7)%48]
	encrypted = drive(map(f,flag),key.decode('hex')).encode('hex')
	return encrypted

# Finding key
key = ''
for i in range(5):
	for s in iter_all_strings():
		if enc(key+s, flag)[:(i*2)+2] == encrypted[:(i*2)+2]:
			key += s
			break

print("key is: {}".format(key))

# Now finding the flag
flag = ""

characters = string.printable

for i in range(len(encrypted)/2+1):
	enc_tmp = encrypted[:i*2]

	for j in characters:
		if enc(key, flag+j.lower()) == enc_tmp:
			flag += j.lower()
print("flag is: {}".format(flag.lower()))
