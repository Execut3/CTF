FROM    ubuntu:16.04

RUN     bash -c "debconf-set-selections <<< 'mysql-server mysql-server/root_password password pass1234pass'"
RUN     bash -c "debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password pass1234pass'"

RUN     apt-get -y update
RUN     apt-get -y install bzip2 libfreetype6 libfontconfig wget \
        build-essential chrpath libssl-dev libxft-dev libfreetype6-dev libfontconfig1 libfontconfig1-dev \
        mysql-server libmysqlclient-dev nginx python python-pip

COPY    website /app  

COPY    scripts/run.sh /run.sh

RUN     chmod +x /run.sh

RUN     service mysql start && service nginx start && \
        cd /app && chmod +x manage.py  && \
        service mysql start && ./manage.py collectstatic --noinput && \
        ./manage.py makemigrations && \
        ./manage.py migrate && \
        ./manage.py initiate_database


#ENTRYPOINT ["/run.sh"]