#AccessLog

**Category:** Web
**Points:** 10

**Description:**

Find the flag in this apache access log

Download: <a href="./access.log.zip">zip file</a>

##AccessLog-Solution:

In this challenges, each user is given a file that contains apache access.log file of a server that is under attack & the flag is send throught content of these messages (by attacker).

most of them are trash except this:

```
192.168.32.1 - - [29/Sep/2015:03:37:34 -0400] "GET /mutillidae/index.php?page=user-info.php&username=%27+union+all+select+1%2CString.fromCharCode%28102%2C+108%2C+97%2C+103%2C+32%2C+105%2C+115%2C+32%2C+83%2C+81%2C+76%2C+95%2C+73%2C+110%2C+106%2C+101%2C+99%2C+116%2C+105%2C+111%2C+110%29%2C3+--%2B&password=&user-info-php-submit-button=View+Account+Details HTTP/1.1" 200 9582 "http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=something&password=&user-info-php-submit-button=View+Account+Details" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
```

first of all, url-decode these request. a usefull tool could be hackbar (mozila extension). So the decoded message will be like this:

```
192.168.32.1 - - [29/Sep/2015:03:37:34 -0400] "GET /mutillidae/index.php?page=user-info.php&username='+union+all+select+1,String.fromCharCode(102,+108,+97,+103,+32,+105,+115,+32,+83,+81,+76,+95,+73,+110,+106,+101,+99,+116,+105,+111,+110),3+--+&password=&user-info-php-submit-button=View+Account+Details HTTP/1.1" 200 9582 "http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=something&password=&user-info-php-submit-button=View+Account+Details" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
```

look like attacker was trying to do a sql injection! and he used ```String.fromCharCode``` to bypass filters. 

```
String.fromCharCode(102,+108,+97,+103,+32,+105,+115,+32,+83,+81,+76,+95,+73,+110,+106,+101,+99,+116,+105,+111,+110)
```

There are a lot of ways to decode this, here is a python solution:

```python
a = '102,+108,+97,+103,+32,+105,+115,+32,+83,+81,+76,+95,+73,+110,+106,+101,+99,+116,+105,+111,+110'
b = a.split(',+')
b = ''.join([chr(int(i)) for i in b])
print b
```

runnig this script will lead to flag, which is:

###flag is SQL_Injection
