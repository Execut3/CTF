#Maze

**Category:** Web
**Points:** 30

**Description:**

There's this friend of mine that got into Real hacking & he also created a webpage. Anyway he is so proud of his website & claim that something's wrong in this webpage that i can't find it out. I check all the Hacking Methods, but I couldn't find anything useful. Can you help me find it out, don't worry in reward i will give you a Flag!

##Maze-Solution:

not ready yet 

**but if you're eager to know, here is a little hint:**

This challenge is created by django/python and is a combination of Http-Method, Request tampering and programming. First of all, this challenge is kind of a mystery, so there are some 
vulnerabilities (or at least pretending to have) that could lead each user to false solution.

1- First, this is not a php project, use something like wappalyzer and you will see that this challenge is created by django on apache.

2- Second, there are hints for sql injection, xss, and vulnerable admin page. but believe me there's nothing out there.

**Note:** The very first step to find holes in a web portal (and to start the proccess of pentesting) is to look for HTTP methods.
There was also a hint in the description of the challenge: ```..... I check all the Hacking Methods, but I ....```.

by simpley sending a post request on main page, there is a hint that says user should have a valid session to access maze.
There is also a hint for a page name ```session.php```. In this page user can get a session and by setting his session id in post request to the first page, he will get a hint that 
he should change his user-agent to ```S3CR37```.

By sending a get request to main.php with ```user-agent:S3CR37```, Az the name "MAZE" represent, this challenge is kind of a maze (imagine pages in /main/ az a maze, user should get to the end of maze by requesting on this pages). users should send get messages to each of inline pages (the 8 pages that are located in /main/ directory).
I appology if the hints in question was not perfectly understandable (cause it was my first held-ctf) but if each of users just tried a little fuzzing in the portal, could find it out so easily.
(Team I.B.N found the door to maze, but somehow they couldn't get the flag)

So after getting a session, user should send a request with tampered user-agent header and then it should look for the next path to go (it could be each of those 8 pages). But there is a problem, if user send a wrong request to a wrong url, it will 
move to first place and should again send a request for main.php and then again start to send reqeust to pages (but this time to another url). 

they should notice that the session will expire after a while. So the only solution is to use scripting. After finding the right path to end of maze, they will get the flag.

```
curl -X POST --cookie "session_id=<cookie recieved from session.php>" http://challenge-address/main
curl -X GET --cookie "session_id=<cookie recieved from session.php>" -A "S3CR37" http://challenge-address/main
# Write a recursive function to get the right path:
curl -X GET --cookie "session_id=<cookie recieved from session.php>" -A "S3CR37" http://challenge-address/main/page=<each of /main/ pages>
#write a bash script to iterate between pages.
```




