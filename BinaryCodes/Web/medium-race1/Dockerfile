FROM    ubuntu:16.04

MAINTAINER Execut3 <execut3@binarycodes.ir>

# Manually set up the apache environment variables
ENV APACHE_RUN_USER="www-data" \
    APACHE_RUN_GROUP="www-data" \
    APACHE_LOG_DIR="/var/log/apache2" \
    APACHE_LOCK_DIR="/var/lock/apache2" \
    APACHE_PID_FILE="/var/run/apache2.pid" \
    MYSQL_DATABASE="race1" \
    MYSQL_ROOT_USER="root" \
    MYSQL_ROOT_PASSWORD="QZohdYALytOUVXgu" \
    MYSQL_USER="race1" \
    MYSQL_PASSWORD="race1@mysqlTYUVNM"

RUN     bash -c "debconf-set-selections <<< 'mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD'"
RUN     bash -c "debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD'"

# Install apache, PHP, and supplimentary programs. openssh-server, curl, and lynx-cur are for debugging the container.
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install \
    apache2 php7.0 php7.0-mysql libapache2-mod-php7.0 curl lynx-cur mysql-server libmysqlclient-dev php-zip unzip

# Enable apache mods.
RUN a2enmod php7.0
RUN a2enmod rewrite

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.0/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.0/apache2/php.ini

# Expose apache.
EXPOSE 80

COPY    ./etc/mysql/mysqld.conf /etc/mysql/mysql.conf.d/mysqld.cnf

COPY    scripts/init.sql /tmp/init.sql
RUN     service mysql start && \
        mysql -uroot -p$MYSQL_ROOT_PASSWORD < /tmp/init.sql && \
        rm /tmp/init.sql

# Copy this repo into place.
ADD app /var/www/site

# Update the default apache site with the config we created.
ADD etc/apache/default /etc/apache2/sites-enabled/000-default.conf

ENV FLAG="flag_8b78e8f7c4e9dd03491ae416a69fb90c"

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD /usr/sbin/apache2ctl -D FOREGROUND && phpenmod zip && \
    service mysql start && service apache2 start && /bin/bash -i
