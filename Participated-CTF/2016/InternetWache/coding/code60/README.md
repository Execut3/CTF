#It's Prime Time!

**Category:** Code
**Points:** 60

**Description:**

We all know that prime numbers are quite important in cryptography. Can you help me to find some?

Service: 188.166.133.53:11059

##It's Prime Time!-Solution:

This challenge is like code50 challenge, The difference is that in this challenge, server will give us
a number, we should find first prime number greater than that and again send that result to server.
This is the output of nc:

```bash
$ nc 188.166.133.53 11059

Hi, you know that prime numbers are important, don't you? Help me calculating the next prime!
Level 1.: Find the next prime number after 8:
```

So i wrote a simple python script, that parse the input, find the number, calculate the first
greater number and sends it again to server.

Here is the python code:

```python
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
```

Script will run for 100 Levels and at last:

```
Recieved number: 37
41
Yay, that's right!
IW{Pr1m3s_4r3_!mp0rt4nt}

```

The flag is: **IW{Pr1m3s_4r3_!mp0rt4nt}**