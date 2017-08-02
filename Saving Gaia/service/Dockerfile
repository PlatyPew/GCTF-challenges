FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python2.7
RUN apt-get install apache2
COPY ./index.html /var/www/index.html
COPY ./notsoeasy.html /var/www/html/notsoeasy.html
COPY ./list.txt /var/www/html/list.txt
COPY ./read.py /var/www/html/read.py
COPY ./view.php /var/www/html/view.php
COPY ./robots.txt /var/www/html/robots.txt
EXPOSE 8000
CMD ["service","apache2","start"]
