#!/bin/sh

docker build -t gaia .
docker run -dt -p 17458:80 --name gaia gaia
docker start gaia
