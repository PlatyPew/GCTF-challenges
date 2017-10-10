FROM python:3-alpine
RUN mkdir -p /opt/chal
COPY ./money_server.py /opt/chal/
WORKDIR /opt/chal
CMD ["python3", "/opt/chal/money_server.py"]
