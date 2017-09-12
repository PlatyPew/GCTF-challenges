#!/bin/sh

docker build -t fishshoops .
docker run -d -p 34567:80 --name fishshoops fishshoops
docker start fishshoops