FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python2.7
RUN useradd -m bashing_pwn
RUN useradd bashing
COPY ./bash.py /home/bashing_pwn/bash.py
COPY ./flag.txt /home/bashing_pwn/flag.txt
COPY ./v13wF1a6 /home/bashing_pwn/.v13wF1a6
RUN chown bashing_pwn /home/bashing_pwn/bash.py
RUN chmod 755 /home/bashing_pwn/bash.py
RUN chown bashing_pwn /home/bashing_pwn/flag.txt
RUN chmod 400 /home/bashing_pwn/flag.txt
RUN chown bashing_pwn /home/bashing_pwn/.v13wF1a6
RUN chmod 4755 /home/bashing_pwn/.v13wF1a6
EXPOSE 2500
CMD ["/usr/bin/python2.7","/home/bashing_pwn/bash.py"]
