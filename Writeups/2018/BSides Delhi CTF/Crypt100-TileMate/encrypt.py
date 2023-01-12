#!/usr/bin/env python2

from itertools import cycle as scooter
from secret import FLAG, KEY
from hashlib import sha384

assert FLAG.islower()
assert len(KEY) == 10

def drive(Helmet, Petrol):
    return ''.join(chr(ord(David)^ord(Toni)) for David,Toni in zip(Helmet,scooter(Petrol)))

f = lambda x: sha384(x).digest()[(ord(x)+7)%48]
encrypted = drive(map(f,FLAG),KEY.decode('hex')).encode('hex')
open('ci.pher.text','wb').write(encrypted)




