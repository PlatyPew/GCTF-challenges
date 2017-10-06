FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install apache2
RUN apt-get -y install php7.0
RUN apt-get -y install libapache2-mod-php7.0
COPY ./gaia.css /var/www/html/.
COPY ./gaia.jpg /var/www/html/.
COPY ./index.html /var/www/html/.
COPY ./list.txt /var/www/html/.
COPY ./notsoeasy.html /var/www/html/.
COPY ./read.py /var/www/html/.
COPY ./robots.txt /var/www/html/.
COPY ./view.php /var/www/html/.
COPY ./view.php.save /var/www/html/.
COPY ./my_journal.txt /var/www/html/.
EXPOSE 80
CMD apachectl -D FOREGROUND
