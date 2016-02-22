#A numbers game II

**Category:** Code
**Points:** 70

**Description:**

Math is used in cryptography, but someone got this wrong. Can you still solve the equations?

Service: 188.166.133.53:11071

##A numbers game II-Solution:

In this challenge, server uses a custom encryption method. This is the output of nc:

```bash
$ nc 188.166.133.53 11071

Hi, I like math and cryptography. Can you talk to me?!
Level 1.: 4.4.5.3.3.3.3.3.3.3.5.6.3.3.3.3.3.4.3.4.3.4.4.6.3.3.3.3.3.4.6.4.3.3.3.3.3.4.3.5.3.4.3.3
```

And we have the source code of the encryption method:

```python
def encode(self, eq):
    out = []
    for c in eq:
        q = bin(self._xor(ord(c),(2<<4))).lstrip("0b")
        q = "0" * ((2<<2)-len(q)) + q
        out.append(q)
    b = ''.join(out)
    pr = []
    for x in range(0,len(b),2):
        c = chr(int(b[x:x+2],2)+51)
        pr.append(c)
    s = '.'.join(pr)
    return s
```

As we can see, each character of input will be converted to ord-number, and will be XORed with number 32 (2<<4 means 32)
and will be saved as binary.

For example for 'a' character the process is like this:

```
ord(a) = 97
q = 97 ^ 32
q = bin(q) = '01000001'
```

These binary values will be saved in 'b' variable. Then in a for statement with step of 2,
each binary value will be convert to base10, Then will be added to 51, and at last will be converted
to character.
So the output are always 3,4,5,6. and these values will be joined using '.'

So our task is clear. we should write a code to decrypt received data from server,
convert it to hex.

This is the python code that i wrote to do this process.

```python
import sys
import socket

ip = '188.166.133.53'
port = 11071


# This is the function that used to encode the clear-text
def encode(eq):
    out = []
    for c in eq:
        q = bin(ord(c)^(2<<4)).lstrip("0b")
        q = "0" * ((2<<2)-len(q)) + q
        out.append(q)
    b = ''.join(out)
    pr = []
    for x in range(0,len(b),2):
        c = chr(int(b[x:x+2],2)+51)
        pr.append(c)
    s = '.'.join(pr)
    return s

substitute_chars = {'3':'00', '4':'01', '5':'10', '6':'11'}

# My function to decode this encryption_method
def decode(eq):
    eq = [i.strip() for i in eq.split('.')]
    result = ''
    for i in range(0,len(eq),4):
        char_num = ''.join(eq[i:i+4])
        char_bin = [substitute_chars[c] for c in char_num]
        char_bin = ''.join(char_bin)
        char_ord = int(char_bin, 2)
        char_xor = chr(int(char_ord)^32)
        result += char_xor
    return result

print decode('4.4.5.3.3.3.3.3.3.3.5.6.3.3.3.3.3.4.3.4.3.4.4.6.3.3.3.3.3.4.6.4.3.3.3.3.3.4.3.5.3.4.4.4')
dsa

def solve_equation(equation):
    params = [i.strip() for i in equation.split(' ')]
    param_1 = int(params[2])
    operator = params[1]
    param_2 = int(params[4])
    
    if operator == '*':
        return param_2/param_1
    elif operator == '/':
        return param_2*param_1
    elif operator == '+':
        return param_2-param_1
    else:
        return param_2+param_1      
       
# Starting Socket proccess here
s = socket.socket()
s.connect((ip,port))
        
while True:
    rec = s.recv(1024)
    if not rec:
        break
    print '%s\n'%rec
    if 'Level' in rec:
        cipher = rec.split(':')[1].strip()
        print 'Recieved cipher: %s'%cipher
        clear = decode(cipher)
        print 'Equation to be solved is: %s'%clear
        result = solve_equation(clear)
        print result
        s.send(str(encode(str(result))))
print 'done'
```

But remember when decoding the result back from server, We are faced with another equation, we should
solve it like code50, and the again encode result with encode() function and send the result
back to server.

Here is output of mine:

```
Recieved cipher: 4.4.5.3.3.3.3.3.3.3.5.5.3.3.3.3.3.4.3.6.3.4.3.5.3.4.4.5.3.3.3.3.3.4.6.4.3.3.3.3.3.4.4.3.3.4.5.3.3.4.3.6.3.4.4.6.3.4.5.3.3.4.4.3
Equation to be solved is: x * 326 = 483784
1484
Yay, that's right!
IW{Crypt0_c0d3}
```

The flag is: **IW{Crypt0_c0d3}**