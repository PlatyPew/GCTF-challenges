#!/bin/sh

docker build -t lecturersays .
docker run -d -p 17451:9999 --name lecturersays lecturersays
docker start lecturersays
