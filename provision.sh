# #!/bin/bash
#
sudo apt-get -y update
#
apt-get install git -y > /dev/null

# Installing MySQL and it's dependencies, Also, setting up root password for MySQL as it will prompt to enter the password during installation
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password sys'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password sys'
sudo apt-get -y install mysql-server

mysql -uroot -psys -e 'create database beerlist;'
mysql -uroot -psys < schema.sql
