#!/bin/sh

docker build -t cookie .
docker run -dt -p 17564:44445 -p 17563:80 --name cookie cookie
docker start cookie