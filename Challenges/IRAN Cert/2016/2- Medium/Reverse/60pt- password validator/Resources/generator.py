#!/usr/bin/python
from os import popen
from os import mkdir
from sys import argv
from random import random as rand
N = int(argv[1])

for t in range(N):
	mkdir('team%d'%t)
	sec=""
	L = 32
	for i in range(L):
		sec += chr(ord('a')+int(rand()*26))
	sec = popen("echo -n %s | md5sum"%sec).read().split(' ')[0]
	open('team%d/flag.txt'%t, 'w+').write(sec)
	# popen("echo 'INSERT INTO `flags` (`teamID`, `taskID`, `flag`) VALUES (%d, 13, '\"'\"%s\"'\"');\' >> rev300.sql"%((t+1), sec))
	sec = list(sec)
	FLAG = 'APACTF{Ok4y_Chi3f_Ug0t_me_again}'
	sec = [i for i in FLAG]
	for i in range(len(sec)):
		sec[i] = chr(ord(sec[i])^0x01)
	sec = "\\\\x".join(['{:02x}'.format(ord(c)) for c in sec])
	rep = "cat rev300.c | sed 's/vi5uZ\\\\\\\\r1s6^1Gz|gM5f hrAui0r/\\\\x%s/'"%(sec)
	source= popen(rep).read()

	f = open('team%d/rev300.c'%t, 'w+')
	f.write(source)
	
