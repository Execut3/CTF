from pwn import *

r = process('average')
# r = remote('hiyoko.quals.seccon.jp', 9001)

r.recv()

n = 16
r.send(f'{n}\n'.encode())

for index in range(n):
	print(r.recv())
	value = '0\n'
	if index == n - 1:
		value = '10'
	r.send(value.encode())

print(r.recv())
# r.interactive()

