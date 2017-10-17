FROM python:3-alpine
RUN mkdir -p /opt/chal
COPY ./coin_server.py /opt/chal/
WORKDIR /opt/chal
CMD ["python3", "/opt/chal/coin_server.py"]
