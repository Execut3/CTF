export MY_USER=root
export MY_PASS=ppass
export MY_HOST=localhost
export MY_DB=ptest
echo "CREATE USER '$MY_USER'@'$MY_HOST' IDENTIFIED BY '$MY_PASS'" | ./bin/mysql -S ./mysql.sock -u root -pdba
echo "CREATE DATABASE $MY_DB" | ./bin/mysql -S ./mysql.sock -uroot -pdba
echo "GRANT ALL ON $MY_DB.* TO '$MY_USER'@'$MY_HOST'" | ./bin/mysql -S ./mysql.sock


CREATE DATABASE  IF NOT EXISTS `xss1` CHARACTER SET UTF8;

CREATE USER xss1_user@localhost IDENTIFIED BY 'xss1_user@pass';

GRANT ALL PRIVILEGES ON xss1.* TO xss1_user@localhost;

FLUSH PRIVILEGES;


./bin/mysql -S ./mysql.sock -u $MY_USER -p$MY_PASS $MY_DB < test.sql



./bin/mysql -S ./mysql.sock -u root -pdba -e "CREATE USER '$MY_USER'@'$MY_HOST' IDENTIFIED BY '$MY_PASS'"
./bin/mysql -S ./mysql.sock -u root -pdba -e "CREATE DATABASE $MY_DB"
./bin/mysql -S ./mysql.sock -u root -pdba -e "GRANT ALL ON $MY_DB.* TO '$MY_USER'@'$MY_HOST'"
./bin/mysql -S ./mysql.sock -D $MY_DB -u $MY_USER -p$MY_PASS -e "SOURCE test.sql"