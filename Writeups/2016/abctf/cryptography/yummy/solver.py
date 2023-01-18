import os, sys
import Image
import binascii

im = Image.open('baconian.bmp')
pix = im.load()
width, height = im.size

binary = ''
for h in range(height):
    for w in range(width):
        binary += '1' if pix[w,h][0] == 0 else '0'
print binary
print '\n'
print binascii.b2a_uu(binary)