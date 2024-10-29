## Temp Questcon 2024 [220pt]

**Category:** Web
**Solves:** 55

## Description
Professor deleted a file !oops Can you find the file for him?

https://questcon-temp.chals.io/


## Solution
We are facing a page with ssrf vuln. we enter url and it will read the url for us. the task is to read the flag from server files.

payload `file://etc/passwd` didn't work.
After some fuzzing be able to read it with `file:///etc//passwd`

Now let's try to read source of code, by some common guesses i find out, source is here:

```
file:///app/app.py
```

and we can see the flag in source code.