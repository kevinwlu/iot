# Django Project "Stevens"

## Start a Django project
```sh
pi@raspberrypi:~ $ django-admin startproject stevens
pi@raspberrypi:~ $ cd stevens
pi@raspberrypi:~/stevens $ ls
```
manage.py  stevens

## Start a Django app
```sh
pi@raspberrypi:~/stevens $ python3 manage.py startapp myapp
pi@raspberrypi:~/stevens $ ls
```
manage.py  myapp  stevens

## Create MySQL database
```sh
pi@raspberrypi:~ $ sudo mysql -u root -p
```
Enter password: PASSWORD

MariaDB [(none)]> use mysql

MariaDB [mysql]> select user, host from mysql.user;

MariaDB [mysql]> create user pi@localhost identified by 'PASSWORD';

MariaDB [mysql]> show databases;

MariaDB [mysql]> create database stevens;

MariaDB [mysql]> grant all privileges on stevens.* to pi@localhost;

MariaDB [mysql]> quit

## Edit settings.py in ~/stevens/stevens

* Follow ~/iot/lesson4/stevens/settings.txt

* Remember to change PASSWORD for MySQL user pi
```sh
pi@raspberrypi:~/stevens $ cd stevens
pi@raspberrypi:~/stevens/stevens $ nano settings.py
```
## Copy urls.py to ~/stevens/stevens
```sh
pi@raspberrypi:~/stevens/stevens $ cp ~/iot/lesson4/stevens/urls.py .
pi@raspberrypi:~/stevens/stevens $ cd ..
```
## Copy admin.py, models.py, and views.py to ~/stevens/myapp
```sh
pi@raspberrypi:~/stevens $ cd myapp
pi@raspberrypi:~/stevens/myapp $ cp ~/iot/lesson4/stevens/admin.py .
pi@raspberrypi:~/stevens/myapp $ cp ~/iot/lesson4/stevens/models.py .
pi@raspberrypi:~/stevens/myapp $ cp ~/iot/lesson4/stevens/views.py .
```
## Copy index.html
```sh
pi@raspberrypi:~/stevens/myapp $ mkdir static templates
pi@raspberrypi:~/stevens/myapp $ cd templates
pi@raspberrypi:~/stevens/myapp/templates $ mkdir myapp
pi@raspberrypi:~/stevens/myapp/templates $ cd myapp
pi@raspberrypi:~/stevens/myapp/templates/myapp $ cp ~/iot/lesson4/stevens/index.html .
```
## Enable Google Maps API

https://cloud.google.com/maps-platform

https://developers.google.com/maps/documentation/javascript/get-api-key

https://churchthemes.com/page-didnt-load-google-maps-correctly

## Edit index.html to add the API key
```sh
pi@raspberrypi:~/stevens/myapp/templates/myapp $ nano index.html
```
## Copy static files
```sh
pi@raspberrypi:~/stevens/myapp/templates/myapp $ cd ~/stevens/myapp/static
pi@raspberrypi:~/stevens/myapp/static $ cp ~/iot/lesson4/static/favicon.ico .
pi@raspberrypi:~/stevens/myapp/static $ mkdir myapp
pi@raspberrypi:~/stevens/myapp/static $ cd myapp
pi@raspberrypi:~/stevens/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
pi@raspberrypi:~/stevens/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
pi@raspberrypi:~/stevens/myapp/static/myapp $ cd ~/stevens
```
## After the first time, skip these three steps if no changes
```sh
pi@raspberrypi:~/stevens $ python3 manage.py makemigrations myapp
pi@raspberrypi:~/stevens $ python3 manage.py migrate
pi@raspberrypi:~/stevens $ python3 manage.py createsuperuser
```
Username (leave blank to use 'pi'):

Email address: EMAIL_ADDRESS

Password: PASSWORD

Password (again): PASSWORD

Superuser created successfully.

## Run Django server
```sh
pi@raspberrypi:~/stevens $ python3 manage.py runserver
```
## Open the Chromium browser on Raspberry Pi via VNC Viewer

### Go to http://127.0.0.1:8000/admin

### Login with Django administration username (pi) and password

### Click temperature data to add 

* Date and time in YYYY-MM-DD HH:MM:SS

* Temperature in Fahrenheit

* Latitude 40.7451

* Longitude -74.0255

### Click SAVE

### View app at http://127.0.0.1:8000
