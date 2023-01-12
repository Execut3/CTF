#!/bin/bash
service mysql start
mysql='mysql -u example_user --password=Admin2015 exampleDB'
for db in `ls /db`; do $mysql < /db/$db; done
rm -r /db
apachectl -k start -e info -DFOREGROUND

cd /var/www/html
git init
git config --global user.email "execut3@binarycodes.ir"
git config --global user.name "Execut3"
git add -A
git commit -m 'initial files added'
