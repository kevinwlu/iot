# Drango REST Project "MyRasPi"

## Start a Django project
```sh
pi@raspberrypi:~ $ django-admin startproject myraspi
pi@raspberrypi:~ $ cd myraspi
pi@raspberrypi:~/myraspi $ ls
```
manage.py  myraspi

## Start a Django app
```sh
pi@raspberrypi:~/myraspi $ python3 manage.py startapp myapp
pi@raspberrypi:~/myraspi $ ls
```
manage.py  myapp  myraspi

## Create MySQL database
```sh
pi@raspberrypi:~ $ sudo mysql -u root -p
```
Enter password: PASSWORD

MariaDB [(none)]> use mysql

MariaDB [mysql]> create user pi@localhost identified by 'PASSWORD';

MariaDB [mysql]> create database myraspi;

MariaDB [mysql]> grant all privileges on myraspi.* to pi@localhost;

MariaDB [mysql]> quit

## Edit settings.py in ~/myraspi/myraspi as in settings.txt
```sh
pi@raspberrypi:~/myraspi $ cd myraspi
pi@raspberrypi:~/myraspi/myraspi $ nano settings.py
```
## Copy urls.py to ~/myraspi/myraspi
```sh
pi@raspberrypi:~/myraspi/myraspi $ cp ~/iot/lesson4/myraspi/urls.py .
pi@raspberrypi:~/myraspi/myraspi $ cd ..
```
## Copy admin.py, models.py, views.py, and serializers.py to ~/myraspi/myapp
```sh
pi@raspberrypi:~/myraspi $ cd myapp
pi@raspberrypi:~/myraspi/myapp $ cp ~/iot/lesson4/myraspi/admin.py .
pi@raspberrypi:~/myraspi/myapp $ cp ~/iot/lesson4/myraspi/models.py .
pi@raspberrypi:~/myraspi/myapp $ cp ~/iot/lesson4/myraspi/views.py .
pi@raspberrypi:~/myraspi/myapp $ cp ~/iot/lesson4/myraspi/serializers.py .
```
## Change the default password 'raspberry' in views.py
```sh
pi@raspberrypi:~/myraspi/myapp $ nano views.py
```
## Copy index.html
```sh
pi@raspberrypi:~/myraspi/myapp $ mkdir static templates
pi@raspberrypi:~/myraspi/myapp $ cd templates
pi@raspberrypi:~/myraspi/myapp/templates $ mkdir myapp
pi@raspberrypi:~/myraspi/myapp/templates $ cd myapp
pi@raspberrypi:~/myraspi/myapp/templates/myapp $ cp ~/iot/lesson4/myraspi/index.html .
```
## Edit index.html to add the Google Maps API key
```sh
pi@raspberrypi:~/myraspi/myapp/templates/myapp $ nano index.html
```
## Copy static files
```sh
pi@raspberrypi:~/myraspi/myapp/templates/myapp $ cd ~/myraspi/myapp/static
pi@raspberrypi:~/myraspi/myapp/static $ cp ~/iot/lesson4/static/favicon.ico .
pi@raspberrypi:~/myraspi/myapp/static $ mkdir myapp
pi@raspberrypi:~/myraspi/myapp/static $ cd myapp
pi@raspberrypi:~/myraspi/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
pi@raspberrypi:~/myraspi/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
pi@raspberrypi:~/myraspi/myapp/static/myapp $ cd ~/myraspi
```
## Copy system_info.py and controller.py to ~/myraspi
```sh
pi@raspberrypi:~/myraspi $ cp ~/iot/lesson3/system_info.py .
pi@raspberrypi:~/myraspi $ cp ~/iot/lesson4/myraspi/controller.py .
```
## Change the default password 'raspberry' in controller.py
```sh
pi@raspberrypi:~/myraspi $ nano controller.py
```
## After the first time, skip these three steps if no changes
```sh
pi@raspberrypi:~/myraspi $ python3 manage.py makemigrations myapp
pi@raspberrypi:~/myraspi $ python3 manage.py migrate
pi@raspberrypi:~/myraspi $ python3 manage.py createsuperuser
```
Username (leave blank to use 'pi'):

Email address: EMAIL_ADDRESS

Password: PASSWORD

Password (again): PASSWORD

Superuser created successfully.

## Run Django server
```sh
pi@raspberrypi:~/myraspi $ python3 manage.py runserver
```
## Open the Chromium browser on Raspberry Pi via VNC Viewer

### At the first time, go to http://127.0.0.1:8000/admin

### Login with Django administration username (pi) and password

### Click location data to add 

* Location Stevens

* Latitude 40.7451

* Longitude -74.0255

### Click SAVE

### Post the following in HTML form:

* 2019-02-21 17:45:00 to the Dt List at http://127.0.0.1:8000/dt

* 50 to the Tmp List at http://127.0.0.1:8000/tmp

* 20 to the Cpu List at http://127.0.0.1:8000/cpu

## Run native controller service on a separate terminal window
```sh
pi@raspberrypi:~/myraspi $ python3 controller.py
```
## View app at http://127.0.0.1:8000/home
