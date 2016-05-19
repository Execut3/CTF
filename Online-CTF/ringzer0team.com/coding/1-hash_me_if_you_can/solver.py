import hashlib
import requests
from bs4 import BeautifulSoup


url = 'https://ringzer0team.com/challenges/13'
headers = {'Cookie':'PHPSESSID=5jico9s6opsh1bhr2ru1l34gk1; _ga=GA1.2.1326342245.1463683440; _gat=1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)
x = soup.find_all("div", class_="message")
message = str(x).split('----- BEGIN MESSAGE -----<br/>')[1].split('----- END MESSAGE -----<br/>')[0].split('<br/>')[0].strip()
digest = hashlib.sha512(message).hexdigest()

r = requests.get(url+'/'+digest, headers=headers)
print r.text

