FROM php:7.0-apache
RUN apt-get update
RUN apt-get -y install python
RUN rm -rf /var/www/html/ && mkdir -p /var/www/html
COPY ./gaia.css /var/www/html/
COPY ./gaia.jpg /var/www/html/
COPY ./index.html /var/www/html/
COPY ./list.txt /var/www/html/
COPY ./notsoeasy.html /var/www/html/
COPY ./read.py /var/www/html/
COPY ./robots.txt /var/www/html/
COPY ./view.php /var/www/html/
COPY ./my_journal.txt /var/www/html
COPY ./view.php.save /var/www/html
COPY ./.htaccess /var/www/html/
