## Direction [100 pts]

**Category:** Web
**Solves:** 188

## Description
Something seems off with the plan displayed on this site. Can you uncover what's hidden behind the scenes and find the way out? The Professor always has a trick up his sleeve. Author: TheProfessor https://questcon-misdirect.chals.io

### Solution

```bash
$ curl "https://questcon-misdirect.chals.io/robots.txt"
User-agent: *
Disallow: /start

$ curl -X POST "https://questcon-misdirect.chals.io/start"
$ curl -X POST "https://questcon-misdirect.chals.io/start" -v
* Request completely sent off
< HTTP/1.1 302 Found
< X-Powered-By: Express
< Location: /redirect0
< X-Flag-Part: QUESTC

$ curl -X GET "https://questcon-misdirect.chals.io/redirect0" -v
< Location: /redirect1
< X-Flag-Part: ON{mi3

$ curl -X GET "https://questcon-misdirect.chals.io/redirect1" -v
< HTTP/1.1 302 Found
< X-Powered-By: Express
< Location: /redirect2
< X-Flag-Part: d1r3ct

$ curl -X GET "https://questcon-misdirect.chals.io/redirect2" -v
< X-Powered-By: Express
< Location: /redirect3
< X-Flag-Part: 10n_15

$ curl -X GET "https://questcon-misdirect.chals.io/redirect3" -v
< HTTP/1.1 302 Found
< X-Powered-By: Express
< Location: /redirect4
< X-Flag-Part: _4n_4r
```
