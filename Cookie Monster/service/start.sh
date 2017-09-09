#!/bin/sh

docker build -t cookie .
docker run -dt -p 44445:44445 -p 44444:80 --name cookie cookie
#docker start cookie