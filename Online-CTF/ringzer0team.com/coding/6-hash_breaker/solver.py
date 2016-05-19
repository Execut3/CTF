import requests
import hashlib
from bs4 import BeautifulSoup


url = 'https://ringzer0team.com/challenges/56'
headers = {'Cookie':'PHPSESSID=5jico9s6opsh1bhr2ru1l34gk1; _ga=GA1.2.1326342245.1463683440; _gat=1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)
x = soup.find_all("div", class_="message")
message = str(x).split('----- BEGIN HASH -----<br/>')[1].split('----- END HASH -----<br/>')[0].split('<br/>')[0].strip()

number = 1000
while True:
    digest = hashlib.sha1(str(number)).hexdigest()
    if digest == message:
        break
    number += 1
result = number

r = requests.get(url+'/'+str(result), headers=headers)
result = BeautifulSoup(r.text)
flag = str(result.find_all("div", class_="alert alert-info"))
print flag

