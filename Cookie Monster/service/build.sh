#!/bin/sh

docker build -t cookie .
docker run -dt -p 17453:44445 -p 17452:80 --name cookie cookie
docker start cookie