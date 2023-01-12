#!/usr/bin/env python

def xor(s1, s2):
    res = [chr(0)]*12
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

def add_pad(msg):
    l = 12 - len(msg)%12
    msg += chr(l)*l
    return msg

with open('flag.png') as f:
    data = f.read()

data = add_pad(data)

with open('key') as f:
    key = f.read()

enc_data = ''
for i in range(0, len(data), 12):
    enc = xor(data[i:i+12], key)
    enc_data += enc

with open('encrypted.png', 'wb') as f:
    f.write(enc_data)
