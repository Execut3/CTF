#Verticode

**Category:** Cryptography

**Description:**

Welcome to Verticode, the new method of translating text into vertical codes.
Each verticode has two parts: the color shift and the code.

The code takes the inputted character and translates it into an ASCII code, and then into binary, then puts that into an image in which each black pixel represents a 1 and each white pixel represents a 0.
For example, A is 65 which is 1000001 in binary, B is 66 which is 1000010, and C is 67 which is 1000011, so the corresponding verticode would look like this.
Except, it isn't that simple.

A color shift is also integrated, which means that the color before each verticode shifts the ASCII code, by adding the number that the color corresponds to, before translating it into binary. In that case, the previous verticode could also look like this.
The table for the color codes is:

0 = Red 1 = Purple 2 = Blue 3 = Green 4 = Yellow 5 = Orange

This means that a red color shift for the letter A, which is 65 + 0 = 65, would translate into 1000001 in binary; however, a green color shift for the letter A, which is 65 + 3 = 68, would translate into 1000100 in binary.
Given this verticode, read the verticode into text and find the flag.

Note that the flag will not be in the typical sctf{flag} format, but will be painfully obvious text. Once you find this text, you will submit it in the sctf{text} format. So, if the text you find is adunnaisawesome, you will submit it as sctf{adunnaisawesome}.

##Solution

```python
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
```

Flag: ```sctf{iamtheflagalllowercasenojoke}```