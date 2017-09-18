#!/bin/sh

docker build -t lecturersays .
docker run -d -p 17457:9999 --name lecturersays lecturersays
#docker start lecturersays
