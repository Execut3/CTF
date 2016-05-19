#Verticode

**Category:** Cryptography

**Description:**

This file describes the input file for "Tracking", and the task you will complete.

Input values:

         +-------+---------------------------+
         | d_{1} | distance from satellite A |
         +-------+---------------------------+
         | d_{2} | distance from satellite B |
         +-------+---------------------------+
         | d_{3} | distance from satellite C |
         +-------+---------------------------+
         | d_{4} | distance from satellite D |
         +-------+---------------------------+

The input file contains the distances in the following order:

                d_{1}, d_{2}, d_{3}, d_{4}

The following system of equations (LaTeX) describes the relationship between
the four distances and the xyz coordinate:

     d_{1}^2=x^2+y^2+z^2
     d_{2}^2=(x-p)^2+y^2+z^2
     d_{3}^2=(x-q)^2+(y-r)^2+z^2
     d_{4}^2=(x-s)^2+(y-t)^2+(z-u)^2

To satisfy the equations above, use this info about the satellites:

     Satellite A lies on the origin          (0, 0, 0)
     Satellite B lies on the x-axis          (p, 0, 0)
     Satellite C lies on the xy-plane        (q, r, 0)
     Satellite D lies on an arbitrary point  (s, t, u)

All satellite locations will be given to you in the input file.

Your task is to calculate the x, y, z coordinates that correspond to each individual line of input, then submit
the average of those values, rounded up.

For Example:

     Coordinate 1: (2, 3, 4)             xAvg = Math.ceil((2 + 2 + 5 + 4 + 5) / 5) = 4
     Coordinate 2: (2, 6, 3)
     Coordinate 3: (5, 2, 3)     --->    yAvg = Math.ceil((3 + 6 + 2 + 2 + 2) / 5) = 3
     Coordinate 4: (4, 2, 4)
     Coordinate 5: (5, 2, 6)             zAvg = Math.ceil((4 + 3 + 3 + 4 + 6) / 5) = 4

              In this example, the flag you submit would be sctf{4, 3, 4}
              
--------------------------------------------------------------------------------------

##Solution

Tracking.in -> file

Begin GPS location info stream...

```python
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
```

flag is: ```sctf{537, 516, 487}```
