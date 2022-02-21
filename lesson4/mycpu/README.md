# Drango REST Project "MyCPU"

## Start a Django project
```sh
~ $ django-admin startproject mycpu
~ $ cd mycpu
~/mycpu $ ls
manage.py  mycpu/
```
## Start a Django app
* Run python3 on Raspberry Pi OS
```sh
~/mycpu $ python manage.py startapp myapp
~/mycpu $ ls
manage.py  myapp/  mycpu/
```
## Edit settings.py in ~/mycpu/mycpu
* Follow ~/iot/lesson4/mycpu/settings.txt, e.g., add an asterisk to ALLOWED_HOSTS as well as myapp and rest_framework to INSTALLED_APPS
```sh
~/mycpu $ cd mycpu
~/mycpu/mycpu $ ls
asgi.py  __init__.py  __pycache__  settings.py  urls.py  wsgi.py
~/mycpu/mycpu $ nano settings.py
```
## Copy urls.py to ~/mycpu/mycpu
```sh
~/mycpu/mycpu $ cp ~/iot/lesson4/mycpu/urls.py .
~/mycpu/mycpu $ cd ..
```
## Copy admin.py, models.py, views.py, and serializers.py to ~/mycpu/myapp
```sh
~/mycpu $ cd myapp
~/mycpu/myapp $ ls
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/admin.py .
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/models.py .
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/views.py .
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/serializers.py .
```
## Change the default password 'admin' in views.py
```sh
~/mycpu/myapp $ nano views.py
```
## Copy index.html
* Default location: Stevens Institute of Technology
```sh
~/mycpu/myapp $ mkdir static templates
~/mycpu/myapp $ cd templates
~/mycpu/myapp/templates $ mkdir myapp
~/mycpu/myapp/templates $ cd myapp
~/mycpu/myapp/templates/myapp $ cp ~/iot/lesson4/mycpu/index.html .
```
## Edit index.html to add the Google Maps API key
* [Application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (API)
* [Google Maps Platform](https://cloud.google.com/maps-platform)
* [Get Google Maps API Key](https://developers.google.com/maps/documentation/javascript/get-api-key)
* [How to fix “This page didn’t load Google Maps correctly” error](https://churchthemes.com/page-didnt-load-google-maps-correctly)
* Alternatively, use [Amap API](https://lbs.amap.com/) that requires registration with a cellphone number in China
  * [AutoNavi](https://en.wikipedia.org/wiki/AutoNavi)
  * [Guide](https://lbs.amap.com/api/javascript-api/guide/abc/prepare)
```sh
~/mycpu/myapp/templates/myapp $ nano index.html
```
## Copy static files
* Stevens favicon: ~/iot/lesson4/static/favicon.ico
* Xidian favicon: ~/iot/lesson4/static/xidian/favicon.ico
```sh
~/mycpu/myapp/templates/myapp $ cd ~/mycpu/myapp/static
~/mycpu/myapp/static $ cp ~/iot/lesson4/static/favicon.ico .
~/mycpu/myapp/static $ mkdir myapp
~/mycpu/myapp/static $ cd myapp
~/mycpu/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
~/mycpu/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
~/mycpu/myapp/static/myapp $ cd ~/mycpu
```
## Copy controller.py to ~/mycpu
```sh
~/mycpu $ ls
db.sqlite3  manage.py  myapp/  mycpu/
~/mycpu $ cp ~/iot/lesson4/mycpu/controller.py .
```
## Change the default password 'admin' in controller.py
```sh
~/mycpu $ nano controller.py
```
## If haven't done so, install (or upgrade) psutil (process and system utilities)
* Run pip3 on Raspberry Pi OS
```sh
~/mycpu $ sudo pip install -U psutil
```
## After the first time, skip these three steps if no changes
* Run python3 on Raspberry Pi OS
* Using Git for Windows, if "python manage.py createsuperuser" leads to "Superuser creation skipped due to not running in a TTY," enter "winpty python manage.py createsuperuser"
```sh
~/mycpu $ python manage.py makemigrations myapp
~/mycpu $ python manage.py migrate
~/mycpu $ python manage.py createsuperuser
Username (leave blank to use '_'): admin
Email address: EMAIL_ADDRESS
Password: admin
Password (again): admin
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
## Run Django server
```sh
~/mycpu $ python manage.py runserver
```
## Open a browser

### At the first time, go to http://127.0.0.1:8000/admin

### Login with Django administration username (admin) and password (admin)

### Click location data to add one of the following
* Location Stevens
  * Latitude 40.7451
  * Longitude -74.0255
* Location Xidian
  * Latitude 34.12250
  * Longitude 108.84029

### Click SAVE

### Post the following in HTML form:

* 2022 to the Dt List at http://127.0.0.1:8000/dt
* 20 to the Cpu List at http://127.0.0.1:8000/cpu
* 20 to the Mem List at http://127.0.0.1:8000/mem

## Run native controller service on a separate terminal window
* If using Git for Windows, enter "winpty python controller.py"
```sh
~/mycpu $ python controller.py
```
## View app at http://127.0.0.1:8000/home

## Alternatively, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0):8000
```sh
~/mycpu $ python manage.py runserver 0.0.0.0:8000
```
## Open a browser on another laptop and go to the server IP address
![mycpu.png](/lesson4/mycpu/mycpu.png)
