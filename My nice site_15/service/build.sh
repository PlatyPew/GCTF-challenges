docker build -t nicesite .
docker run -dt -p 17566:80 --name nicesite nicesite
docker start nicesite
