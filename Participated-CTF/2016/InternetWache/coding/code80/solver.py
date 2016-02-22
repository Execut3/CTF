__author__ = 'Execut3'
import socket
import time
from datetime import datetime
import hashlib
import string

ip = '188.166.133.53'
port = 11117

flag = ''

s = socket.socket()
s.connect((ip,port))

my_list = string.printable
brute_list = []
for current in xrange(2):
    a = [i for i in my_list]
    for y in xrange(current):
        a = [x+i for i in my_list for x in a]
    brute_list = brute_list + a

def convert_to_epoch(this_time):
    date = '21.02.2016 '
    this_time = this_time.strip()
        
    date_time = date + this_time
    pattern = '%d.%m.%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    epoch -= 21582
    print epoch
    epoch_list = range(epoch-100 ,epoch+1000)  
    
    return epoch_list 

def crack_hash(epoch_list, given_hash):
    global flag
    for epoch in epoch_list:
        for char in brute_list:
            hash_object = hashlib.sha1(str(epoch)+':'+char)
            this_hash = hash_object.hexdigest()
            if this_hash == given_hash:
                flag += char
                return str(epoch)+':'+char
    return ''


while True:
    rec = s.recv(1024)
    if not rec:
        break
    # print '%s\n'%rec
    if 'Char' in rec:
        for j in rec.split('\n'):
            if 'Char' in j:
                recc = j
                break
        this_time = recc.split(',')[0].split(' ')[-1].strip()
        print 'Recieved time: %s'%this_time
        this_hash = recc.split(':')[-1].strip()
        print 'Received hash: %s'%this_hash
        epoch_list = convert_to_epoch(this_time)
        result = crack_hash(epoch_list, this_hash)
        print result
        s.send(result)
print 'done'
print 'flag is: %s'%flag


# People say, you're good at brute forcing...
# Hint: Format is TIME:CHAR
# Char 0: Time is 19:33:21, 052th day of 2016 +- 30 seconds and the hash is: b3007e6bb4ae0e4ff58c719fc11fa89f8cb4cb78


# flag is: IW{M4N_Y0U_C4N_B3_BF_M4T3RiAL!}