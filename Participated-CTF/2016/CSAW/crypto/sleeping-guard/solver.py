from socket import socket
from base64 import b64decode
from itertools import cycle, izip


def read_line(s):
    try:
        buffer = s.recv(1)
        rec = ''
    
        while buffer != '\n':
            rec += buffer
            buffer = s.recv(1)
        return rec
    except:
        return rec
    
    
def get_next_char(string, index):
    l = len(string)
    # print string[(index+1)%l]
    return string[(index+1)%l]


def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))


address = 'crypto.chal.csaw.io'
port = 8000
s = socket()
s.settimeout(1)
s.connect((address,port))

png_header = '89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52'
png_trailer = '49 45 4E 44 AE 42 60 82'
png_header_chars = [i.decode('hex') for i in png_header.split(' ')]
png_trailer_chars = [i.decode('hex') for i in png_trailer.split(' ')]


out_file = open('result', 'w')

image =  read_line(s)
# print result
# result = b64decode(result)
# out_file.write(result)


# image = open('test', 'r').read()
image = b64decode(image)

key = ''
for i in range(len(image[:16])):
    xored = xor_strings(image[i], png_header_chars[i])
    key += xored
print key
key = 'WoAh_A_Key!?'

message = ''.join(chr(ord(c)^ord(k)) for c,k in izip(image, cycle(key)))
with open('image.png', 'w') as o:
    o.write(message)
    




