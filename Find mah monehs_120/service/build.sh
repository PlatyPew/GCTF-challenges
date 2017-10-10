#!/bin/sh
docker build -t money .
docker run --restart always --memory 64M -d -p 17454:13337 --name money money
docker start money
