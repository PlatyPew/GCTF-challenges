FROM python:3-alpine
RUN mkdir -p /opt/chal
COPY ./lecturer_says.py /opt/chal/
COPY ./commands.txt /opt/chal/
WORKDIR /opt/chal
CMD ["python3", "/opt/chal/lecturer_says.py"]
