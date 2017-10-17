#!/bin/sh
echo "Building Fish Shoups"
docker build -t fishshoups .
docker run --restart always --memory 256M -d -p 17562:80 --name fishshoups fishshoups
docker start fishshoups
