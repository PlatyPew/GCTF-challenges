FROM ubuntu:latest
ENV user1=bashing
ENV user2=bashing_pwn
RUN apt-get update
RUN apt-get install -y python2.7
RUN apt-get install -y xinetd
RUN useradd -m $user2
RUN useradd $user1
RUN echo "$user1     hard    nproc       20" >> /etc/security/limits.conf
COPY ./bash.py /home/$user2/bash.py
COPY ./flag.txt /home/$user2/flag.txt
COPY ./v13wF1a6 /home/$user2/.v13wF1a6
COPY ./bashingservice /etc/xinetd.d/bashingservice
RUN chown $user2 /home/$user2/bash.py
RUN chmod 755 /home/$user2/bash.py
RUN chown $user2 /home/$user2/flag.txt
RUN chmod 400 /home/$user2/flag.txt
RUN chown $user2 /home/$user2/.v13wF1a6
RUN chmod 4755 /home/$user2/.v13wF1a6
EXPOSE 25000
CMD ["/usr/sbin/xinetd","-d"]
