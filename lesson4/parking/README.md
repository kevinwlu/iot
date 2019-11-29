# Django REST Project "Parking"

This project needs a ultrasonic distance sensor HC-SR04:

https://www.adafruit.com/product/3942

## Start a Django project
```sh
pi@raspberrypi:~ $ django-admin startproject parking
pi@raspberrypi:~ $ cd parking
pi@raspberrypi:~/parking $ ls
```
manage.py  parking

## Start a Django app
```sh
pi@raspberrypi:~/parking $ python3 manage.py startapp myapp
pi@raspberrypi:~/parking $ ls
```
manage.py  myapp  parking

## Create MySQL database
```sh
pi@raspberrypi:~ $ sudo mysql -u root -p
```
Enter password: PASSWORD

MariaDB [(none)]> use mysql

MariaDB [mysql]> create user pi@localhost identified by 'PASSWORD';

MariaDB [mysql]> create database parking;

MariaDB [mysql]> grant all privileges on parking.* to pi@localhost;

MariaDB [mysql]> quit

## Edit settings.py in ~/parking/parking

* Follow ~/iot/lesson4/parking/settings.txt

* Remember to change PASSWORD for MySQL user
```sh
pi@raspberrypi:~/parking $ cd parking
pi@raspberrypi:~/parking/parking $ nano settings.py
```
## Copy urls.py to ~/parking/parking
```sh
pi@raspberrypi:~/parking/parking $ cp ~/iot/lesson4/parking/urls.py .
pi@raspberrypi:~/parking/parking $ cd ..
```
## Copy models.py, views.py, and serializers.py to ~/parking/myapp
```sh
pi@raspberrypi:~/parking $ cd myapp
pi@raspberrypi:~/parking/myapp $ cp ~/iot/lesson4/parking/models.py .
pi@raspberrypi:~/parking/myapp $ cp ~/iot/lesson4/parking/views.py .
pi@raspberrypi:~/parking/myapp $ cp ~/iot/lesson4/parking/serializers.py .
```
## Change the default password 'raspberry' in views.py
```sh
pi@raspberrypi:~/parking/myapp $ nano views.py
```
## Copy index.html
```sh
pi@raspberrypi:~/parking/myapp $ mkdir static templates
pi@raspberrypi:~/parking/myapp $ cd templates
pi@raspberrypi:~/parking/myapp/templates $ mkdir myapp
pi@raspberrypi:~/parking/myapp/templates $ cd myapp
pi@raspberrypi:~/parking/myapp/templates/myapp $ cp ~/iot/lesson4/parking/index.html .
```
## Copy static files
```sh
pi@raspberrypi:~/parking/myapp/templates/myapp $ cd ~/parking/myapp/static
pi@raspberrypi:~/parking/myapp/static $ cp ~/iot/lesson4/static/favicon.ico .
pi@raspberrypi:~/parking/myapp/static $ mkdir myapp
pi@raspberrypi:~/parking/myapp/static $ cd myapp
pi@raspberrypi:~/parking/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
pi@raspberrypi:~/parking/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
pi@raspberrypi:~/parking/myapp/static/myapp $ cp ~/iot/lesson4/static/*png .
pi@raspberrypi:~/parking/myapp/static/myapp $ cd ~/parking
```
## Copy controller.py to ~/parking
```sh
pi@raspberrypi:~/parking $ cp ~/iot/lesson4/parking/controller.py .
```
## Change the default password 'raspberry' in controller.py
```sh
pi@raspberrypi:~/parking $ nano controller.py
```
## After the first time, skip these three steps if no changes
```sh
pi@raspberrypi:~/parking $ python3 manage.py makemigrations myapp
pi@raspberrypi:~/parking $ python3 manage.py migrate
pi@raspberrypi:~/parking $ python3 manage.py createsuperuser
```
Username (leave blank to use 'pi'):

Email address: EMAIL_ADDRESS

Password: PASSWORD

Password (again): PASSWORD

Superuser created successfully.

## Terminal 1: Run Django server
```sh
pi@raspberrypi:~/parking $ python3 manage.py runserver
```
## Open the Chromium browser on Raspberry Pi via VNC Viewer

## At the first time, post the following in HTML form:

* empty to the state list at http://127.0.0.1:8000/state

## Terminal 2: Run native controller service
```sh
pi@raspberrypi:~/parking $ sudo python3 controller.py
```
## View app at http://127.0.0.1:8000/home
