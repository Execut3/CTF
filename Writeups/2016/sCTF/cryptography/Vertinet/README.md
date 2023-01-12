#Vertinet

**Category:** Cryptography

**Description:**

This problem follows the same specifications as the previous Verticode problem, except that you have to solve many of them by developing a client to communicate with the server available at problems1.2016q1.sctf.io:50000. Good luck.

##Solution

python solution:

```python
import Image
from PIL import ImageFile
import socket
import os
from binascii import a2b_base64
from bs4 import BeautifulSoup
import base64

ImageFile.LOAD_TRUNCATED_IMAGES = True

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)


def decode_image():
    im = Image.open('image.png')
    pix = im.load()
    w = im.size[0]
    h = im.size[1]
    print w,h
    step = 12
    
    text = ''
    for row in range(h/step):
        this_byte = bytearray()
        for column in range((w/step)-8,w/step):
            this_pix = pix[column*step, row*step]
            if column == 6:
                if this_pix == (255, 255, 0):
                    type = 4
                elif this_pix == (255, 165, 0):
                    type = 5
                elif this_pix == (128, 0, 128):
                    type = 1
                elif this_pix == (0, 128, 0):
                    type = 3
                elif this_pix == (255, 0, 0):
                    type = 0
                else:
                    type = 2
                # print this_pix
                continue
            bit = 0 if this_pix == (255, 255, 255) else 1
            this_byte.append(bit)
        this_byte = ''.join(["{0:b}".format(x) for x in this_byte])
        this_ascii = chr(int(this_byte,2)-type)
        text += this_ascii
        # raw_input('Enter')
    return text


def recvall(sock):
    data = ""
    part = None
    while part != "":
        part = sock.recv(4096)
        data += part
        if '</img>' in data:
            break
    return data


ip = 'problems1.2016q1.sctf.io'
port = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(1)
s.connect((ip,port))

while True:
    html_data = recvall(s)
    print html_data
    soap = BeautifulSoup(html_data)
    img = soap.find("img")['src']
    img = ''.join(img.split('base64,')[1:])
    binary_data = decode_base64(img)
    os.popen('rm -rf image.png')
    fd = open('image.png', 'wb')
    fd.write(binary_data)
    fd.close()
    decoded = decode_image()
    s.send(decoded)
```

Flag: ```sctf{y0ub34tth3v3rt1c0d3}```