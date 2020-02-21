# <a href="https://goo.gl/bhktY0">Lesson 4</a>: Django and Flask

## Labs A and B: Django and Django REST

### Install Django and Django REST framework
```sh
$ pip3 -V
$ sudo pip3 install -U setuptools
$ sudo pip3 install -U django
$ sudo pip3 install -U djangorestframework
$ sudo pip3 install -U django-filter
$ sudo pip3 install -U markdown
$ sudo pip3 install -U requests
```
### Install MariaDB server and client
```sh
$ sudo apt update
$ sudo apt install mariadb-server mariadb-client
$ sudo apt install python3-mysqldb
$ sudo pip3 install -U mysqlclient
$ sudo mysql_secure_installation
```
### Install psutil (process and system utilities)
```sh
$ sudo pip3 install -U psutil
```
### Install Adafruit_Python_DHT library
```sh
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ sudo python3 setup.py install
$ cd
```
### Install Adafruit_Python_BMP library
```sh
$ git clone https://github.com/adafruit/Adafruit_Python_BMP.git
$ cd Adafruit_Python_BMP
$ sudo python3 setup.py install
$ cd
```
### Install Adafruit_Python_ADXL345 library
```sh
$ git clone https://github.com/adafruit/Adafruit_Python_ADXL345.git
$ cd Adafruit_Python_ADXL345
$ sudo python3 setup.py install
$ cd
```
### Follow the instructions for Django projects stevens, weather, myraspi, lighting, parking, and sensing

## Lab C: Flask

### Install Flask-Ask and Ngrok
```sh
$ sudo pip3 install -U flask-ask
$ sudo pip3 install 'cryptography<2.2'
$ sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
$ sudo unzip ngrok-stable-linux-arm.zip
```
## Lab D: LAMP

### Install Apache web server and PHP
```sh
$ sudo apt update
$ sudo apt install apache2
$ sudo service apache2 restart
```
### Open a Chromium browser and go to http://127.0.0.1 to view the Apache2 Debian Default Page
```sh
$ sudo apt install php7.3
$ cd /var/www/html
$ ls
$ sudo mv index.html index.html.bak
$ sudo cp ~/iot/lesson4/index.php .
$ sudo service apache2 restart
```
### Open a Chromium browser and go to http://127.0.0.1 to view "Hello world!" and the PHP info

### Build a Linux-Apache-MySQL-PHP (LAMP) web server with WordPress 
```sh
$ sudo apt install php7.3-mysql
$ cd /var/www/html
$ sudo chown pi: .
$ mv index.php index.php.bak
$ wget http://wordpress.org/latest.tar.gz
$ tar xzf latest.tar.gz
$ mv wordpress/* .
$ rm -rf wordpress latest.tar.gz
$ cd
```
### Create database and grant all privileges
```sh
$ sudo mysql -u root -p
```
Enter password: PASSWORD

MariaDB [(none)]> use mysql

MariaDB [mysql]> create database wordpress;

MariaDB [mysql]> grant all privileges on wordpress.* to pi@localhost;

MariaDB [mysql]> quit
```sh
$ sudo service apache2 restart
```
### Open a Chromium browser and go to http://127.0.0.1 to configure Wordpress
```sh
$ nano wp-config.php
```
### Copy the highlighted text, paste it, save wp-config.php, and run the installation
