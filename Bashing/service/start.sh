#!/bin/sh
docker build -t bashing .
docker run -dt -p 25000:25000 --name bashing bashing
docker start bashing
