cipher = 'IVyN5U3X)ZUMYCs'
flag = ''

for i in cipher:
    flag += chr(ord(i)^cipher.index(i))

print 'flag is: %s'%flag