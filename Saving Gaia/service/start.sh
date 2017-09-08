#!/bin/sh

docker build -t gaia .
docker run -dt -p 33333:80 --name gaia gaia
#docker start gaia
