#!/bin/sh
docker build -t coin .
docker run --restart always --memory 64M -d -p 17452:31337 --name coin coin
docker start coin
