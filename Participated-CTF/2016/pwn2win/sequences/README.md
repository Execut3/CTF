#sequences

**Category:** PPC

##Solution

server gave us a sequence of numbers in each line, we should find the type of that sequence like fibunacci,lucas... (i googled for them) and then find the given position in that sequence and then send it back to server in format result1,result2,...

```python
import socket

def tribonacci(number, a0=0, a1=0, a2=1):
    n = [a0, a1, a2]
    while len(n) <= number:
        n.append(n[-3]+n[-2]+n[-1])
    return n

def sum_sequence(n1, n2, number):
    n = [int(n1), int(n2)]
    while len(n) <= int(number):
        n.append(n[-1]+(n[-1]-n[-2]))
    return n

def lucas(n):
    result = [2, 1]
    for i in range(n):
        result.append(result[-2]+result[-1])
    return result

def LCM(n1, n2, number):
    result = [n1, n2]
    factor = n2 / n1
    while len(result) < number:
        result.append(result[-1]*factor)
    return result

def fib2(n):
    result = []
    a, b = 0, 1
    count = 1
    while count <= n:
        result.append(b)
        a, b = b, a+b
        count += 1
    return result

lucas_list = lucas(130)
tribunacci_001 = tribonacci(130, 0,0,1)
fib2_list = fib2(130)

def find_result(position, sequences):
    n1 = int(sequences[0])
    n2 = int(sequences[1])
    n3 = int(sequences[2])
    position = int(position)
    if n2 + (n2-n1) == n3:
        print 'SUM'
        seq = sum_sequence(n1, n2, 130)
        index = seq.index(n1)
        return seq[index+position-1]
    elif n1 in lucas_list and n2 in lucas_list and n3 in lucas_list:
        print 'Lucas'
        index = lucas_list.index(n1)
        return lucas_list[position+index-1]
    elif n1 in tribunacci_001 and n2 in tribunacci_001 and n3 in tribunacci_001:
        print 'Tribunacci'
        index = tribunacci_001.index(n1)
        return tribunacci_001[position+index-1]
    elif n1 in fib2_list and n2 in fib2_list and n3 in fib2_list:
        print 'Fibunacci'
        index = fib2_list.index(n1)
        return fib2_list[position+index-1]
    elif n3%n2 == 0 and n2 %n1 ==0:
        print 'LCM'
        lcm_list = LCM(n1, n2, 130)
        index = lcm_list.index(n1)
        return lcm_list[position+index-1]
    return False


flag = ''
ip = 'pool.pwn2win.party'
port = 1337
s = socket.socket()
s.connect((ip,port))

rec = ''
b = s.recv(1024)
while not 'Results' in b:
    rec += b
    b = s.recv(1024)
    print b
    
line = []
counter = 0
rec = rec.split('\n')
for i in rec:
    if i:
        tmp = {}
        tmp['index'] = counter
        tmp['position'] = int(i.split('-')[0].strip())
        tmp['sequences'] = [j.strip() for j in i.split(' - ')[1].split('->')]
        counter += 1
    line.append(tmp)
line = line[:-1]


Result = []
for l in line:
    result = find_result(l['position'], l['sequences'])
    Result.append(result)
# print Result

Result = [str(i) for i in Result]
s.send(','.join(Result)+'\n')
print s.recv(1024)
print 'GOT FLAG'
```

flag is: ```CTF-BR{Agor4_j4_pod3m0s_com3c4r_4_br1nc4r_d3_v3rd4d3-by_Skypitain82!\m/}```
