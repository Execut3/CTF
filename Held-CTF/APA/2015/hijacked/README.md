#Hijacked

**Category:** Web
**Points:** 30
**Description:**

I don't like this friend of mine named john. he is administrator of a webpage. and i really hate this guy. yesterday i sniff through his network and could capture him while he was logging into his account. So i beg you visit this page:http://172.27.221.13/login.php and find his password so i can just throw this pass on his face. here is the pcap file of what is sniffed yesterday!!! 
<a href="./hijacked.pcap.pcapng">pcap file</a>

##Hijacked-Solution

This challenges is a combination of network forensics, source reading, lfi vulnerability, bypassing lfi custom prevention filters and at last session cracking.

Based on the story of the challenge, a person with real name john created a webpage and before he uploaded his webpage on his host server, his network was sniffed by his friend (the attacker). By sniffing his network his friend(the attacker) found john’s session when john was opening his profile page(as admin). 

So the job of each user is to find this session, login into the website, find the lfi vulnerability, read the source of php file that creates session and at last find the password of john. So let’s start:

###looking at the pcap file

Fire up wireshark. Based on the story of challenge, the file was captured before john uploaded his files on the server. So we should find a way to see which stream is the one that we are looking for.

The name of the challenge is 'hijacked', this is a clue. So let’s set a filter on this name:

```wireshark-filter:	frame contains "hijacked"```

And we see that he was opening welcome.php page on ip address 192.168.32.134. Click on packet and follow tcp stream. you will see that john sends a GET request for http://192.168.32.134/ctf_challenge/hijacked/welcome.php . and tadah, we see that there is a CTF_Session cookie in the stream. 

![Image of 1]
(./Images/1.png)

```CTF_Session = 1944593278175d7565e2421726462d5bb5f2141675d6433420405d6412322790534152557d37```

Note: some of users may say that how we know we should set a filter on ‘hijacked’ string? the answer is you shouldn’t know, cause you need to find it out. Simply by looking at the hijacked.iutcert.io and looking at pages, you could find the list of pages for this web. So simple filtering on all of this pages names one by one, will simply give you the result. 

Anyway, after finding the session, it’s time to check the website. by opening webpage, you will see a login page like this:

![Image of 2]
(./Images/2.png)