FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install php7.0
RUN apt-get -y install libapache2-mod-php7.0
RUN apt-get -y install python
RUN apt-get -y install libfontconfig
COPY ./cookiemonsteronly.php /var/www/html/.
COPY ./index.html /var/www/html/.
COPY ./showImage.php /var/www/html/.
COPY ./phantomjs /tmp/.
COPY ./cookie.txt /tmp/.
COPY ./image.js /tmp/.
COPY ./run.py /tmp/.
COPY ./setup.sh /tmp/.
EXPOSE 80 44445
WORKDIR /tmp
ENTRYPOINT ["bash","setup.sh"]

