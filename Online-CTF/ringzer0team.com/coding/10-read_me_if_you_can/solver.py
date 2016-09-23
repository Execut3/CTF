import requests
import base64
from bs4 import BeautifulSoup
from captcha_solver import CaptchaSolver

url = 'https://ringzer0team.com/challenges/17'
headers = {'Cookie':'PHPSESSID=5jico9s6opsh1bhr2ru1l34gk1; _ga=GA1.2.1326342245.1463683440; _gat=1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)
x = soup.find_all("div", class_="message")
message = str(x).split('----- IMAGE -----<br/>')[1].strip()
m = message.split('src="')[1].split('"/><br/>')[0].strip()

# print m
# captcha = open('captcha.png', 'w')
# captcha.write(m.split('base64,')[1])
# captcha.close()

solver = CaptchaSolver('browser')
captcha = open('captcha.png', 'rb').read()
print(solver.solve_captcha(captcha))
# print m

r = requests.get(url+'/'+str(result), headers=headers)
result = BeautifulSoup(r.text)
flag = str(result.find_all("div", class_="flag"))
print flag

