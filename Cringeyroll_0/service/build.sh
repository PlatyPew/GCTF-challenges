#!/bin/sh

docker build -t cringeyroll .
docker run -d -p 17122:80 --name cringeyroll cringeyroll
docker start cringeyroll
