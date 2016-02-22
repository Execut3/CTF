#A numbers game

**Category:** Code
**Points:** 50

**Description:**

People either love or hate math. Do you love it? Prove it! You just need to solve a bunch of equations without a mistake.

Service: 188.166.133.53:11027

##A numbers game-Solution:

The challenge is simple. We make a conection, Server asks us a bunch of equation, we should solve them and
send the answer. There are 100 levels. Here is the result for nc:

```bash
$nc 188.166.133.53 11027

Hi, I heard that you're good in math. Prove it!
Level 1.: x * 14 = 238
```

So i wrote a simple python script, that parse the input, find the equation and solve it and sends the
result to server again until it receives the flag.

Here is the python code:

```python
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
```

Script will run for 100 Levels and at last:

```
Recieved equation: x * 953 = 1297986
Yay, that's right!
IW{M4TH_1S_34SY}
```

The flag is: **IW{M4TH_1S_34SY}**