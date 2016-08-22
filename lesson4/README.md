# Lesson 4: Django

pi@raspberrypi:~ $ sudo apt-get update

pi@raspberrypi:~ $ sudo apt-get dist-upgrade

pi@raspberrypi:~ $ sudo reboot

pi@raspberrypi:~ $ sudo apt-get install python-dev

pi@raspberrypi:~ $ wget https://bootstrap.pypa.io/get-pip.py

pi@raspberrypi:~ $ sudo python get-pip.py

pi@raspberrypi:~ $ sudo pip install -U pip

pi@raspberrypi:~ $ sudo pip install -U setuptools

pi@raspberrypi:~ $ sudo pip install -U django

pi@raspberrypi:~ $ sudo pip install -U djangorestframework

pi@raspberrypi:~ $ sudo pip install -U django-filter

pi@raspberrypi:~ $ sudo pip install -U markdown

pi@raspberrypi:~ $ sudo pip install -U requests

pi@raspberrypi:~ $ sudo apt-get install mysql-server mysql-client

pi@raspberrypi:~ $ sudo apt-get install python-mysqldb

pi@raspberrypi:~ $ mysql -u root -p
Enter password:

mysql> create database stevens;
Query OK, 1 row affected (0.00 sec)

mysql> create database parking;
Query OK, 1 row affected (0.00 sec)

mysql> create database sensing;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| parking            |
| performance_schema |
| sensing            |
| stevens            |
+--------------------+
6 rows in set (0.00 sec)

mysql> quit
Bye

pi@raspberrypi:~ $ sudo apt-get install python-mysqldb
