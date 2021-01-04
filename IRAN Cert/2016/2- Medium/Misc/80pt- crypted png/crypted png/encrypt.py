import binascii

def get_bytes_from_file(filename):  
    return open(filename, "rb").read()


inp = get_bytes_from_file("./flag.png")
key = '****'
key *= len(inp)/len(key)

inp_int = int(binascii.hexlify(inp),16)
key_int = int(binascii.hexlify(key),16)
xor = inp_int ^ key_int
output = binascii.unhexlify('{0:x}'.format(xor))


d = open('flag_encrypted.png','wb')
d.write(output)
d.close()