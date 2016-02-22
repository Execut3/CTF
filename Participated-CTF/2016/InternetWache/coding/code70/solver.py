__author__ = 'Execut3'
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