FROM alpine:latest

# Update packages
RUN apk --update upgrade && \
    apk add \
        apache2 \
        mysql \
        mysql-client \
        php5 \
        php5-apache2 \
        php5-mysqli

# Prepare directories
RUN mkdir -p /run/apache2/ && \
    mkdir -p /run/mysqld/

# Move source folder
COPY ./src /var/www/localhost/htdocs/

# Move setup script
COPY ./setup.sh /

RUN chmod 755 /setup.sh

# Set entrypoint
CMD /setup.sh
