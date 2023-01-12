import Image
im = Image.open('code1.png').convert('RGB')
pix = im.load()
w = im.size[0]
h = im.size[1]
print w,h
step = 12

flag_text = ''
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
    flag_text += this_ascii
    # raw_input('Enter')
    
print flag_text

# 0 = Red
# 1 = Purple
# 2 = Blue
# 3 = Green
# 4 = Yellow
# 5 = Orange


# sctf{iamtheflagalllowercasenojoke}