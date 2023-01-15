#!/usr/bin/env python3

from Crypto.Util.number import *
import string

flag = 'ASIS{this_might_be_the_flag}'

def is_valid(s, p):
	return True

def random_str(l):
	rstr = ''
	for _ in range(l):
		rstr += string.printable[:94][getRandomRange(0, 93)]
	return rstr

def encrypt(msg, nbit):
	l, p = len(msg), getPrime(nbit)
	rstr = random_str(p - l)
	# print(rstr)
	msg += rstr
	while True:
		s = getRandomNBitInteger(1024)
		print(s)
		if is_valid(s, p):
			break
	enc = msg[0]
	print(enc)
	for i in range(p-1):
		print(f'{s}, {i}, {p}')
		print(pow(s, i, p))
		enc += msg[pow(s, i, p)]
	return enc

nbit = 15
enc = encrypt(flag, nbit)
# print(f'enc = {enc}')
