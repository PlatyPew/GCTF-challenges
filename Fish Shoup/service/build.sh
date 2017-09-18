#!/bin/sh

docker build -t fishshoups .
docker run -d -p 17456:80 --name fishshoups fishshoups
docker start fishshoups
