#!/bin/sh

docker build -t lecturersays .
docker run -d -p 9999:9999 --name lecturersays lecturersays
#docker start lecturersays
