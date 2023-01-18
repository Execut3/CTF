import requests
import base64
from bs4 import BeautifulSoup
import hashlib
url = 'https://ringzer0team.com/challenges/57'
headers = {'Cookie':'PHPSESSID=5jico9s6opsh1bhr2ru1l34gk1; _ga=GA1.2.1326342245.1463683440; _gat=1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)
x = soup.find_all("div", class_="message")
m_hash = str(x).split('----- BEGIN HASH -----<br/>')[1].split('----- END HASH -----<br/>')[0].split('<br/>')[0].strip()

number = 1000
while number < 10000:
    digest = hashlib.sha1(str(number)+m_salt).hexdigest()
    if digest == m_hash:
        break
    number += 1
result = number

r = requests.get(url+'/'+str(result), headers=headers)
result = BeautifulSoup(r.text)
flag = str(result.find_all("div", class_="alert alert-info"))
print flag

