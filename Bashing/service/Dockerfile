FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python
RUN useradd -m bashing
COPY ./bash.py /home/bashing/.
COPY ./f14g /home/bashing/.
COPY ./thisisareallylongflagbutifyoucansomehowcatthisitwouldbeamazing /bin/.
RUN chmod 755 /home/bashing/bash.py
RUN chmod 755 /home/bashing/f14g
RUN chmod 755 /bin/thisisareallylongflagbutifyoucansomehowcatthisitwouldbeamazing
RUN chmod 755 /tmp
USER bashing
WORKDIR /home/bashing
EXPOSE 25000
CMD ["python","/home/bashing/bash.py"]
