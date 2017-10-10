#!/bin/sh
docker build -t gaia .
docker run --restart always --memory 128M -d -p 17565:80 --name gaia gaia
docker start gaia
