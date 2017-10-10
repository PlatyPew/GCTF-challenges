FROM alpine:latest
RUN apk update
RUN apk add apache2 mysql mysql-client php5 php5-apache2 php5-mysqli
RUN mkdir -p /run/apache2/
RUN mkdir -p /run/mysqld/
RUN mkdir -p /opt/chal
RUN rm -rf /var/www/localhost/htdocs/ && mkdir -p /var/www/localhost/htdocs/
COPY ./src /var/www/localhost/htdocs/
COPY ./entrypoint.sh /opt/chal/
RUN chmod +x /opt/chal/entrypoint.sh
CMD /opt/chal/entrypoint.sh
