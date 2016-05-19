from PIL import Image
import os, sys
path = './'

operation = sys.argv[3]
im1_name = sys.argv[1]
im2_name = sys.argv[2]
output_name = sys.argv[4]

img1 = Image.open(path+im1_name).convert('L')
img1 = img1.point(lambda x: 0 if x<128 else 255, '1')
img2 = Image.open(path+im2_name).convert('L')
img2 = img2.point(lambda x: 0 if x<128 else 255, '1')

img1_pix = img1.load()
img2_pix = img2.load()
mx,my = img2.size

output = Image.new('L', (mx,my))
output_pix = output.load()

for i in range(mx):
    for j in range(my):
        if operation == 'add':
            output_pix[i,j] = img1_pix[i,j] + img2_pix[i,j]
        elif operation == 'mul':
            output_pix[i,j] = img1_pix[i,j] * img2_pix[i,j]
        elif operation == 'sub':
            output_pix[i,j] = img1_pix[i,j] - img2_pix[i,j]
        if output_pix[i,j] == 255:
            output_pix[i,j] = 255
        if output_pix[i,j] < 0:
            output_pix[i,j] = 0

output.save('./output/'+output_name, "PNG")
# output.show()