# Django Project "Xidian"

## Start a Django project
```sh
~ $ django-admin startproject xidian
~ $ cd xidian
~/xidian $ ls
manage.py  xidian/
```

## Start a Django app
```sh
~/xidian $ python manage.py startapp myapp
~/xidian $ ls
manage.py  myapp/  xidian/
```

## Edit settings.py in ~/xidian/xidian

* Follow ~/iot/lesson4/xidian/settings.txt

```sh
~/xidian $ cd xidian
~/xidian/xidian $ ls
asgi.py  __init__.py  __pycache__  settings.py  urls.py  wsgi.py
~/xidian/xidian $ nano settings.py
```
## Copy urls.py to ~/xidian/xidian
```sh
~/xidian/xidian $ cp ~/iot/lesson4/stevens/urls.py .
~/xidian/xidian $ cd ..
```
## Copy admin.py, models.py, and views.py to ~/xidian/myapp
```sh
~/xidian $ cd myapp
~/xidian/myapp $ ls
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
~/xidian/myapp $ cp ~/iot/lesson4/stevens/admin.py .
~/xidian/myapp $ cp ~/iot/lesson4/stevens/models.py .
~/xidian/myapp $ cp ~/iot/lesson4/stevens/views.py .
```
## Copy index.html
```sh
~/xidian/myapp $ mkdir static templates
~/xidian/myapp $ cd templates
~/xidian/myapp/templates $ mkdir myapp
~/xidian/myapp/templates $ cd myapp
~/xidian/myapp/templates/myapp $ cp ~/iot/lesson4/stevens/index.html .
```
## Enable Maps API
* [Application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (API)
* [Google Maps Platform](https://cloud.google.com/maps-platform)
* [Get Google Maps API Key](https://developers.google.com/maps/documentation/javascript/get-api-key)
* [How to fix “This page didn’t load Google Maps correctly” error](https://churchthemes.com/page-didnt-load-google-maps-correctly)
* Alternatively, use [Amap API](https://lbs.amap.com/) that requires registration with a cellphone number in China
  * [AutoNavi](https://en.wikipedia.org/wiki/AutoNavi)
  * [Guide](https://lbs.amap.com/api/javascript-api/guide/abc/prepare)

## Edit index.html to add the Maps API key, and change from "Stevens Institute of Technology" to "Xidian University" and from "F" (Fahrenheit) to "C" (Celsius)
```sh
~/xidian/myapp/templates/myapp $ nano index.html
```
## Copy static files
```sh
~/xidian/myapp/templates/myapp $ cd ~/xidian/myapp/static
~/xidian/myapp/static $ cp ~/iot/lesson4/static/xidian/favicon.ico .
~/xidian/myapp/static $ mkdir myapp
~/xidian/myapp/static $ cd myapp
~/xidian/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
~/xidian/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
~/xidian/myapp/static/myapp $ cd ~/xidian
```
## After the first time, skip these three steps if no changes
* From Git Bash on Windows, if "python manage.py createsuperuser" leads to "Superuser creation skipped due to not running in a TTY," enter "winpty python manage.py createsuperuser"
```sh
~/xidian $ python manage.py makemigrations myapp
~/xidian $ python manage.py migrate
~/xidian $ python manage.py createsuperuser
Username (leave blank to use '_'): admin
Email address: EMAIL_ADDRESS
Password: PASSWORD
Password (again): PASSWORD
Superuser created successfully.
```
## Run Django server
```sh
~/xidian $ python manage.py runserver
```
## Open a browser

### Go to http://127.0.0.1:8000/admin

### Login with Django administration username (admin) and PASSWORD

### Click temperature data to add 

* Date and time in YYYY-MM-DD HH:MM:SS

* Temperature in Celsius

* Latitude 34.12250

* Longitude 108.84029

### Click SAVE

### View app at http://127.0.0.1:8000

## Alternatively, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0):8000
```sh
~/xidian $ python manage.py runserver 0.0.0.0:8000
```
## Open a browser on another laptop and go to the server IP address

![xidian.png](/lesson4/xidian/xidian.png)
