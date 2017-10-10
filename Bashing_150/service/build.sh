#!/bin/sh
docker build -t bashing .
docker run --restart always --memory 128M -dt -p 17345:25000 --name bashing bashing
docker start bashing
