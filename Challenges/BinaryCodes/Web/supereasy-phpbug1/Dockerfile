FROM    ubuntu:16.04

MAINTAINER Execut3 <execut3@binarycodes.ir>

# Install apache, PHP, and supplimentary programs. openssh-server, curl, and lynx-cur are for debugging the container.
RUN apt-get update && apt-get install apache2 php7.0 libapache2-mod-php7.0 -y

# Enable apache mods.
RUN a2enmod php7.0
RUN a2enmod rewrite

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.0/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.0/apache2/php.ini

# Expose apache.
EXPOSE 80

# Copy this repo into place.
ADD app /var/www/site

# Update the default apache site with the config we created.
ADD etc/apache/default /etc/apache2/sites-enabled/000-default.conf

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD /usr/sbin/apache2ctl -D FOREGROUND && \
    service apache2 start && /bin/bash -i
