def xor(s1, s2):
    res = [chr(0)]*12
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
        # print res
    res = ''.join(res)
    return res


enc_png = open('encrypted.png', 'rb').read()
# png_header = ''.join([chr(i) for i in [137, 80, 78, 71, 13, 10, 26, 10]])
png_header = '89504E470D0A1A0A0000000D49484452'.decode('hex')
key = xor(enc_png[:12], png_header[:12])

    
enc_data = ''
for i in range(0, len(enc_png), 12):
    enc = xor(enc_png[i:i+12], key)
    enc_data += enc

with open('output.png', 'wb') as output:
    output.write(enc_data)
    output.close()
