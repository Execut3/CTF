__author__ = 'Execut3'
import socket

ip = '188.166.133.53'
port = 11027

s = socket.socket()
s.connect((ip,port))

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
    
        

while True:
    rec = s.recv(1024)
    if not rec:
        break
    print '%s\n'%rec
    if 'Level' in rec:
        equation = rec.split(':')[1].strip()
        print 'Recieved equation: %s'%equation
        x = solve_equation(equation)
        s.send(str(x))
print 'done'