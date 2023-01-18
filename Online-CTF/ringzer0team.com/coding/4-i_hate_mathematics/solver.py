import requests
from bs4 import BeautifulSoup


url = 'https://ringzer0team.com/challenges/32'
headers = {'Cookie':'PHPSESSID=5jico9s6opsh1bhr2ru1l34gk1; _ga=GA1.2.1326342245.1463683440; _gat=1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)
x = soup.find_all("div", class_="message")
message = str(x).split('----- BEGIN MESSAGE -----<br/>')[1].split('----- END MESSAGE -----<br/>')[0].split('<br/>')[0].strip()
message = message.split('=')[0].strip()
m = message.split(' ')
message = ''

for i in m:
    if '0x' in i:
        message += str(int(i,16))
    else:
        try:
            message += str(int(i,2))
        except:
            message += i    
result = eval(message)

r = requests.get(url+'/'+str(result), headers=headers)
result = BeautifulSoup(r.text)
flag = str(result.find_all("div", class_="alert alert-info"))
print flag

