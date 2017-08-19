#!/bin/sh
docker build -t bashing .
docker run -dt -p 2500:2500 bashing
