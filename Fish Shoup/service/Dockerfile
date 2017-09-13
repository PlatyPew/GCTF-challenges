FROM linode/lamp:latest
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install php5-mysql
RUN rm -rfd /var/www/example.com
RUN rm /etc/apache2/sites-enabled/example.com.conf
RUN rm /etc/apache2/sites-available/example.com.conf
RUN rm /var/www/html/index.html
RUN rmdir /var/www/html
ADD ./src /var/www
COPY ./setup.sh /
ENTRYPOINT ["bash","/setup.sh"]
EXPOSE 80
