FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python
RUN useradd -m bashing
COPY ./bash.py /home/bashing/.
COPY ./thisisaverylongflagbutineedittobethislongsothatpeoplecannotbruteforceit.txt /home/bashing/.
RUN chown root:bashing /home/bashing/bash.py
RUN chmod 755 /home/bashing/bash.py
RUN chown root:bashing /home/bashing/thisisaverylongflagbutineedittobethislongsothatpeoplecannotbruteforceit.txt
RUN chmod 440 /home/bashing/thisisaverylongflagbutineedittobethislongsothatpeoplecannotbruteforceit.txt
RUN chown root:bashing /home/bashing
RUN chmod 755 /home/bashing
RUN chmod 755 /tmp
USER bashing
WORKDIR /home/bashing
EXPOSE 25000
CMD ["python","/home/bashing/bash.py"]
