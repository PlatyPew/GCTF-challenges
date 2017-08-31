#!/bin/sh

docker build -t money .
docker run -d -p 13337:13337 --name money money
docker start money
