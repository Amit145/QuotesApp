#!/bin/bash  

#update system repositories 
apt update  

#install Curl 
apt install curl -y  

#install docker compose 
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 
chmod +x /usr/local/bin/docker-compose 
docker-compose --version

#Install Docker
apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
apt install docker-ce -y
usermod -aG docker ${USER}
systemctl start docker 

#build docker compose
cd ./QuotesAppAPI
docker-compose build

#run
docker-compose up
