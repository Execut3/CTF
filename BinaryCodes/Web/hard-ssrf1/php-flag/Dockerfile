FROM linode/lamp

MAINTAINER Execut3 <execut3@binarycodes.ir>

RUN apt-get update; apt-get install php5-mysql git -y

ADD html /var/www/html
ADD data/db /db
ADD start.sh /start.sh
ADD apache /etc/apache2/sites-enabled
CMD ["bash", "/start.sh"]
