#!/bin/sh

docker build -t gaia .
docker run -dt -p 8000:8000 gaia
