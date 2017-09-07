FROM php:7.0-apache
RUN apt-get update
RUN apt-get install -y python2.7
COPY ./gaia.css /var/www/html/.
COPY ./gaia.jpg /var/www/html/.
COPY ./index.html /var/www/html/.
COPY ./list.txt /var/www/html/.
COPY ./notsoeasy.html /var/www/html/.
COPY ./read.py /var/www/html/.
COPY ./robots.txt /var/www/html/.
COPY ./view.php /var/www/html/.
CMD ["service","apache2","start"]
