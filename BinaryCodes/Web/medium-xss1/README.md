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


