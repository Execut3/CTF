## Tile Mate

**Category:** Crypto **Points:** 100

### Solution

By looking at encryptor.py, we know that:

- key is 5 characters (10 hex)

- flag starts with ```flag{```, so we can find key by bruting over first 10 hex values of encrypted in the file.

- after finding the key, we should find next values of flag, one by one simply by bruting over printable characters (It's a simple for over printable ascii's)

- Remember flag values should contain lower values.

Here is the solution:

```python
#!/usr/bin/env python2
import string, itertools

from itertools import cycle as scooter
from hashlib import sha384

# We know this is first 5 characters of flag.
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
```
