import requests
import hashlib
from bs4 import BeautifulSoup


url = 'https://ringzer0team.com/challenges/119'
headers = {'Cookie':'PHPSESSID=5jico9s6opsh1bhr2ru1l34gk1; _ga=GA1.2.1326342245.1463683440; _gat=1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)
x = soup.find_all("div", class_="message")
message = str(x).split('----- BEGIN MESSAGE -----<br/>')[1].split('----- END MESSAGE -----<br/>')[0].strip()
m = message.split('<br/>')[1:]

# for i in xrange(0, len(m), 6):
#     for j in m[i:i+6]:
#         print j
    
result = ''
i = -1
while i < len(m):
    i += 1
    try:
        if not m[i]:
            continue
        if m[i] == 'xxxxx':
            result += '5'
        elif m[i] == '\xc2\xa0xx\xc2\xa0\xc2\xa0':
            result += '1'
        elif m[i] == '\xc2\xa0xxx\xc2\xa0':
            # if m[i+1] == 'x\xc2\xa0\xc2\xa0\xc2\xa0x':
            if m[i+2] == 'x\xc2\xa0\xc2\xa0\xc2\xa0x':
                result += '0'
            elif m[i+2] == '\xc2\xa0\xc2\xa0xx\xc2\xa0':
                if m[i+3] == 'x\xc2\xa0\xc2\xa0\xc2\xa0x':
                    result += '3'
                else:
                    result += '2'
        else:
            result += '4'
        i += 4
    except IndexError:
        break

r = requests.get(url+'/'+str(result), headers=headers)
result = BeautifulSoup(r.text)
flag = str(result.find_all("div", class_="flag"))
print flag

