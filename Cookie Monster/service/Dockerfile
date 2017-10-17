FROM php:7.0-apache
RUN apt-get update
RUN apt-get -y install python libfontconfig wget
RUN rm -rf /var/www/html/ && mkdir -p /var/www/html
COPY ./cookiemonsteronly.php /var/www/html/
COPY ./index.html /var/www/html/
COPY ./showImage.php /var/www/html/
COPY ./.htaccess /var/www/html/
WORKDIR /tmp
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 -O phantom && tar xvfj phantom && mv phantom*/bin/phantomjs . && rm -rf phantom phantomjs-2.1.1*
RUN apt-get -y purge wget && apt-get -y autoremove
COPY ./cookie.txt /tmp/
COPY ./image.js /tmp/
COPY ./run.py /tmp/
COPY ./entrypoint.sh /tmp/
RUN chmod 755 /tmp/entrypoint.sh
EXPOSE 44445
RUN service apache2 start
ENTRYPOINT ["/tmp/entrypoint.sh"]
