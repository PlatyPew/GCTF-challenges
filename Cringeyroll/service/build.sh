#!/bin/sh

docker build -t cringeyroll .
docker run -d -p 17454:80 --name cringeyroll cringeyroll
docker start cringeyroll
