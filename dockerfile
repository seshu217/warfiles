FROM
MAINTAINER
RUN
CMD
ENTRYPOINT
LABELS
USER
WORKDIR
VOLUMES
docker build -t imagename .
docker run --name c1 -it ubuntu
apt-get update
apt-get install -y tomcat
docker commit containername imagename
docker-compose
version: '3'
services:
 mydb:
  image: mysql
  environment:
   MYSQL_ROOT_PASSWORD: seshu
 mywordpress:
  image: wordpress
  port:
   - 8888:80
  links:
   - mydb:mysql
docker networks
docker network create amma
docker network create nanna
docker run --name webserver -d -P --link nanna websever
docker container ls
docker images
docker network ls

