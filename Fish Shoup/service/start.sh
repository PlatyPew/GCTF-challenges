#!/bin/sh

docker build -t fishshoups .
docker run -d -p 34567:80 --name fishshoups fishshoups
docker start fishshoups
