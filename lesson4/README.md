# <a href="https://goo.gl/bhktY0">Lesson 4</a>: Django and Flask

# Labs A and B: Django and Django REST

## Install Django and Django REST framework

pip3 -V

sudo pip3 install -U setuptools

sudo pip3 install -U django

sudo pip3 install -U djangorestframework

sudo pip3 install -U django-filter

sudo pip3 install -U markdown

sudo pip3 install -U requests

## Install MySQL server and client

sudo apt-get update

sudo apt-get install mysql-server mysql-client

sudo apt-get install python3-mysqldb

sudo mysql_secure_installation

## Install psutil (process and system utilities)

sudo pip3 install psutil

## Install Adafruit_Python_DHT library

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT

sudo python3 setup.py install

cd

## Install Adafruit_Python_BMP library

git clone https://github.com/adafruit/Adafruit_Python_BMP.git

cd Adafruit_Python_BMP

sudo python3 setup.py install

cd

# Lab C: Flask

## Install Flask-ask and Ngrok

sudo pip3 install -U flask-ask

sudo pip3 install 'cryptography<2.2'

sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip

sudo unzip ngrok-stable-linux-arm.zip

./ngrok http 5000

# Lab D: LAMP

## Install Apache web server and PHP

sudo apt-get update

sudo apt-get install apache2

sudo service apache2 restart

### Open a Chromium browser and go to http://127.0.0.1 to view the Apache2 Debian Default Page

sudo apt-get install php7.0

cd /var/www/html

ls

sudo mv index.html index.html.bak

sudo cp ~/iot/lesson4/index.php .

sudo service apache2 restart

### Open a Chromium browser and go to http://127.0.0.1 to view "Hello world!" and the PHP info

## Build a Linux-Apache-MySQL-PHP (LAMP) web server with WordPress 

sudo apt-get install php7.0-mysql

cd /var/www/html

sudo chown pi: .

mv index.php index.php.bak

wget http://wordpress.org/latest.tar.gz

tar xzf latest.tar.gz

mv wordpress/* .

rm -rf wordpress latest.tar.gz

cd

### Create database and grant all privileges

sudo mysql -u root -p

Enter password: PASSWORD

MariaDB [(none)]> use mysql

MariaDB [mysql]> create database wordpress;

MariaDB [mysql]> grant all privileges on wordpress.* to pi@localhost;

MariaDB [mysql]> quit

sudo service apache2 restart

### Open a Chromium browser and go to http://127.0.0.1 to configure Wordpress

nano wp-config.php

### Copy the highlighted text, paste it, save wp-config.php, and run the installation
