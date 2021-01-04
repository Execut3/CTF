CREATE DATABASE  IF NOT EXISTS `xss1` CHARACTER SET UTF8;

CREATE USER xss1_user@localhost IDENTIFIED BY 'xss1_user@pass';

GRANT ALL PRIVILEGES ON xss1.* TO xss1_user@localhost;

FLUSH PRIVILEGES;