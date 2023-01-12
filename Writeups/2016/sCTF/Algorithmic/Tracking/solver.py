
my_file = open('raw_data.dat', 'r').read()
data = my_file.split('\n')

# A: (0, 0, 0)
# B: (2000, 0, 0)
# C: (2000, 2000, 0)
# D: (3000, 1500, 1700)

def ceil(n):
    res = int(n)
    return res if res == n or n < 0 else res+1

p = 2000
q = 2000
r = 2000
s = 3000
t = 1500
u = 1700

x_list = []
y_list = []
z_list = []
for line in data:
    if line:
        d = [float(i.strip().strip('\r')) for i in line.split(' ')]
        #print d
        x = ( (d[0]*d[0]) - (d[1]*d[1]) + (p**2)) / (2*p)
        y = ( ( (d[0]*d[0]) - (d[2]*d[2]) + (q**2) + (r**2) ) / (2*r) ) - ( (q*x)/r )
        z = ( ( (d[0]*d[0]) - (d[3]*d[3]) + (s**2) + (t**2) + (u**2) ) / (2*u) ) - ( (s*x)/u ) - ( (t*y)/u )
        x_list.append(int(x))
        y_list.append(int(y))
        z_list.append(int(z))
x_avg = ceil(float(sum(x_list))/len(x_list))
y_avg = ceil(float(sum(y_list))/len(y_list))
z_avg = ceil(float(sum(z_list))/len(z_list))
print 'sctf{%i, %i, %i}'%(x_avg, y_avg, z_avg)