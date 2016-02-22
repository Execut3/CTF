__author__ = 'Execut3'
import socket

ip = '188.166.133.53'
port = 11059

s = socket.socket()
s.connect((ip,port))

def find_prime(start):
    number = start
    state = False
    while not state:
        number = number + 1
        state = True
        for i in range(2, number/2):
            if number % i == 0:
                state = False
                break
    return number
        
while True:
    rec = s.recv(1024)
    if not rec:
        break
    print '%s\n'%rec
    if 'Level' in rec:
        number = rec.split(':')[1].split('after')[-1].strip()
        print 'Recieved number: %s'%number
        prime = find_prime(int(number))
        print prime
        s.send(str(prime))
print 'done'


