#!/bin/sh

docker build -t cringeyroll .
docker run -d -p 30000:80 --name cringeyroll cringeyroll
docker start cringeyroll