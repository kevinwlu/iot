# <a href="https://goo.gl/bhktY0">Lesson 4</a>: Django and Flask

# Install Django and Django REST framework

sudo pip3 install -U setuptools

sudo pip3 install -U django

sudo pip3 install -U djangorestframework

sudo pip3 install -U django-filter

sudo pip3 install -U markdown

sudo pip3 install -U requests

# Install and run MySQL server and client

sudo apt-get install mysql-server mysql-client

sudo mysql_secure_installation

sudo mysql -u root -p

MariaDB [mysql]> select user, host from mysql.user;

MariaDB [mysql]> create user pi@localhost identified by 'PASSWORD';

MariaDB [mysql]> show databases;

MariaDB [mysql]> create database myraspi;

MariaDB [mysql]> grant all privileges on myraspi.* to pi@localhost;

sudo apt-get install python3-mysqldb

# Start a Django project/app and run server

django-admin startproject stevens

cd stevens

python3 manage.py startapp myapp

python3 manage.py makemigrations myapp

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

# Install Flask-ask and Ngrok

sudo pip3 install -U flask-ask

sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip

sudo unzip ngrok-stable-linux-arm.zip

./ngrok http 5000

# Install Apache web server and PHP

sudo apt-get update

sudo apt-get install apache2

sudo service apache2 restart

sudo apt-get install php7.0 libapache2-mod-php7.0

sudo service apache2 restart

# Build a Linux-Apache-MySQL-PHP (LAMP) web server with WordPress 

sudo apt-get install php7.0-mysql

cd /var/www/html

sudo chown pi: .

mv index.php index.php.bak

wget http://wordpress.org/latest.tar.gz

tar xzf latest.tar.gz

mv wordpress/* .

rm -rf wordpress latest.tar.gz

cd

mysql -u root -p

sudo service apache2 restart

# Install psutil (process and system utilities)

sudo pip3 install −U psutil

