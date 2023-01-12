# Initiate:
```bash
docker run -it -p 10000:80 -v "$(pwd)":/var/www/site ctf/race1 bash
service mysql start
service apache2 start
```
visit setup.php, then corrupt setup.php that nobody can interact with it,
and remove the flag section from the bottom of it.
test a user register and login and done...