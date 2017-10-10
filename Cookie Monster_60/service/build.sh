#!/bin/sh
docker build -t cookiemonster .
docker run --restart always --memory 128M -d -p 17564:44445 -p 17563:80 --name cookiemonster cookiemonster
docker start cookiemonster
