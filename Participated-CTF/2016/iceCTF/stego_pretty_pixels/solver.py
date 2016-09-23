from PIL import Image
import binascii

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

img = Image.open('solved.bmp')
pix = img.load()
w,h = img.size

flag_bits = ''
for i in range(w):
    for j in range(h):
        flag_bits += '1' if pix[i,j][0] == 255 else '0'
print text_from_bits(flag_bits)