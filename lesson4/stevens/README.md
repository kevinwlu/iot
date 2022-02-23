# Django Project "Stevens"

## Start a Django project
```sh
pi@raspberrypi:~ $ django-admin startproject stevens
pi@raspberrypi:~ $ cd stevens
pi@raspberrypi:~/stevens $ ls
manage.py  stevens
```

## Start a Django app
```sh
pi@raspberrypi:~/stevens $ python3 manage.py startapp myapp
pi@raspberrypi:~/stevens $ ls
manage.py  myapp  stevens
```

## Create MySQL database
* On Windows or macOS, use the default SQLite database instead of MariaDB
```sh
pi@raspberrypi:~ $ sudo mysql -u root -p
Enter password: PASSWORD
MariaDB [(none)]> use mysql
MariaDB [mysql]> select user, host from mysql.user;
MariaDB [mysql]> create user pi@localhost identified by 'PASSWORD';
MariaDB [mysql]> show databases;
MariaDB [mysql]> create database stevens;
MariaDB [mysql]> grant all privileges on stevens.* to pi@localhost;
MariaDB [mysql]> quit
```
## Edit settings.py in ~/stevens/stevens

* Follow ~/iot/lesson4/stevens/settings.txt, e.g., add myapp to INSTALLED_APPS

* Remember to change PASSWORD for MySQL user pi
```sh
pi@raspberrypi:~/stevens $ cd stevens
pi@raspberrypi:~/stevens/stevens $ ls
asgi.py  __init__.py  __pycache__  settings.py  urls.py  wsgi.py
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
pi@raspberrypi:~/stevens/myapp $ ls
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
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

[Application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (API)

https://cloud.google.com/maps-platform

https://developers.google.com/maps/documentation/javascript/get-api-key

https://churchthemes.com/page-didnt-load-google-maps-correctly

## Edit index.html to add the Google Maps API key
* Without a valid API key, the map is darkened and watermarked with “this page didn’t load Google maps correctly”
* Substitute YOUR_API_KEY in index.html with the API key
```sh
pi@raspberrypi:~/stevens/myapp/templates/myapp $ nano index.html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
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
* Using Git for Windows, if "python manage.py createsuperuser" leads to "Superuser creation skipped due to not running in a TTY," enter "winpty python manage.py createsuperuser"
```sh
pi@raspberrypi:~/stevens $ python3 manage.py makemigrations myapp
pi@raspberrypi:~/stevens $ python3 manage.py migrate
pi@raspberrypi:~/stevens $ python3 manage.py createsuperuser
Username (leave blank to use 'pi'):
Email address: EMAIL_ADDRESS
Password: PASSWORD
Password (again): PASSWORD
Superuser created successfully.
```
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

## On Raspberry Pi with an asterisk in ALLOWED_HOSTS of settings.py, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0):8000
```sh
pi@raspberrypi:~/stevens $ python3 manage.py runserver 0.0.0.0:8000
```
## Open a laptop browser and go to the Raspbbery Pi IP address as opposed to the localhost

![stevens.png](/lesson4/stevens/stevens.png)
