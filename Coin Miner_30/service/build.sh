#!/bin/sh

docker build -t coin .
docker run -d -p 17452:31337 --name coin coin
docker start coin
