import subprocess
from PIL import Image
import requests
import os

base_url = "http://i-hate-captchas.ctf.nsec.ir/"
captcha_url = base_url + 'captcha.php'
index_url = base_url + 'index.php'
check_url = base_url + 'check.php'

def image_remove_noises():
    im = Image.open("captcha.png")
    im = im.convert("P")
    hist = im.histogram()
    
    im2 = Image.new("P",im.size,255)
    im = im.convert("P")
    temp = {}
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            temp[pix] = pix
            if pix in range(110, 136):
                im2.putpixel((y,x),0)
    
    im2.save("output.png")
    im2 = im2.resize((400,100),Image.ANTIALIAS)
    im2.convert("RGB")
    im2.save("output2.png")


r = requests.get(captcha_url)
session = dict(PHPSESSID=r.cookies["PHPSESSID"])
# session = {'PHPSESSID': 'ho1gava71u8fqnem5ljastn4d2'}


for xx in range(301):
    print session
    r = requests.get(captcha_url, cookies=session)
    a = open("captcha.png","w")
    print "[+] Captcha received"
    a.write(requests.utils.get_unicode_from_response(r))
    a.close()
    image_remove_noises()

    subprocess.call("tesseract output2.png out -psm 8",shell=True)
    x = open("out.txt").read()
    x = x.replace("\n","")#[::-1]
    print "Sending: %s"%x
    datas = {"answer":x.replace("\n",""),"Submit":"Submit"}
    r = requests.get(check_url)
    headers = r.headers
    
    postdata = {"answer":x,"Submit":"Submit"}
    s = requests.session()
    r = s.post(check_url,data=postdata,cookies=session)
    print r.content
