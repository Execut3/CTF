import socket
import hashlib
import itertools
import string

def recvline(s):
    buf = ""
    while not buf.endswith("\n"):
        buf += s.recv(1)
    return buf

address = 'rabit.pwning.xxx'
port = 7763
s = socket.socket()
s.connect((address, port))
print recvline(s)
text = recvline(s)
# text = 'Give me a string starting with v7UrlqYt2a, of length 15, such that its sha1 sum ends in ffffff'
print text

start_string = text.split(',')[0].split(' ')[-1].strip()
end_string = 'ffffff'
repeat = 15 - len(start_string)
print 'String = %s'%start_string

captcha = ''
for i in itertools.product('abcdefghijklmnopqrstuvwxyz0123456789', repeat=repeat):
    word = start_string + ''.join(i)
    
    sha1 = hashlib.sha1(word).hexdigest()
    if sha1[-6:] == end_string:
        captcha = word
        print '[+] Found sha1 %s'%captcha
        break
        
if captcha:
    s.send(captcha+'\n')
    rec = recvline(s)
    print rec
    N = rec.split('=')[1].strip()
    print 'N = %s\n'%N
    rec = recvline(s)
    flag = rec.split(':')[1].split('\n')[0].strip()
    print 'flag = %s\n'%flag
    
    r = raw_input('cipher: ')
    s.send(r+'\n')
    print s.recv(1024)
    while True:
        r = raw_input('cipher: ')
        s.send(r+'\n')
        print recvline(s)
    