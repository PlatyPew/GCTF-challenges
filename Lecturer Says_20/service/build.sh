#!/bin/sh
echo "Building Lecturer Says"
docker build -t lecturersays .
docker run --restart always --memory 64M -d -p 17451:9999 --name lecturersays lecturersays
docker start lecturersays
