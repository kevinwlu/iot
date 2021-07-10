# Drango REST Project "MyCPU"

## Start a Django project
```sh
~ $ django-admin startproject mycpu
~ $ cd mycpu
~/mycpu $ ls
manage.py  mycpu/
```
## Start a Django app
```sh
~/myraspi $ python manage.py startapp myapp
~/myraspi $ ls
manage.py  myapp/  mycpu/
```
## Edit settings.py in ~/mycpu/mycpu
* Follow ~/iot/lesson4/mycpu/settings.txt
```sh
~/mycpu $ cd myraspi
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
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/admin.py .
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/models.py .
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/views.py .
~/mycpu/myapp $ cp ~/iot/lesson4/mycpu/serializers.py .
```
## Change the default password 'raspberry' in views.py
```sh
~/mycpu/myapp $ nano views.py
```
## Copy index.html
```sh
~/mycpu/myapp $ mkdir static templates
~/mycpu/myapp $ cd templates
~/mycpu/myapp/templates $ mkdir myapp
~/mycpu/myapp/templates $ cd myapp
~/mycpu/myapp/templates/myapp $ cp ~/iot/lesson4/mycpu/index.html .
```
## Edit index.html to add the Google Maps API key
* Alternatively, use [Amap API](https://lbs.amap.com/) (see [AutoNavi](https://en.wikipedia.org/wiki/AutoNavi))
```sh
~/mycpu/myapp/templates/myapp $ nano index.html
```
## Copy static files
```sh
~/mycpu/myapp/templates/myapp $ cd ~/mycpu/myapp/static
~/mycpu/myapp/static $ cp ~/iot/lesson4/static/xidian/favicon.ico .
~/mycpu/myapp/static $ mkdir myapp
~/mycpu/myapp/static $ cd myapp
~/mycpu/myapp/static/myapp $ cp ~/iot/lesson4/static/*css .
~/mycpu/myapp/static/myapp $ cp ~/iot/lesson4/static/*js .
~/mycpu/myapp/static/myapp $ cd ~/mycpu
```
## Copy controller.py to ~/myraspi
```sh
~/mycpu $ cp ~/iot/lesson4/mycpu/controller.py .
```
## Change the default password 'raspberry' in controller.py
```sh
~/mycpu $ nano controller.py
```
## If haven't done so, install (or upgrade) psutil (process and system utilities)
```sh
~/mycpu $ sudo pip3 install -U psutil
```
## After the first time, skip these three steps if no changes
* From Git Bash on Windows, if "python manage.py createsuperuser" leads to "Superuser creation skipped due to not running in a TTY," enter "winpty python manage.py createsuperuser"
```sh
~/mycpu $ python manage.py makemigrations myapp
~/mycpu $ python manage.py migrate
~/mycpu $ python manage.py createsuperuser
Username (leave blank to use '_'): admin
Email address: EMAIL_ADDRESS
Password: admin
Password (again): admin
Superuser created successfully.
```
## Run Django server
```sh
~/mycpu $ python manage.py runserver
```
## Open a browser

### At the first time, go to http://127.0.0.1:8000/admin

### Login with Django administration username (admin) and password (admin)

### Click location data to add 

* Location Xidian
* Latitude 34.12250
* Longitude 108.84029

### Click SAVE

### Post the following in HTML form:

* 2021 to the Dt List at http://127.0.0.1:8000/dt
* 20 to the Cpu List at http://127.0.0.1:8000/cpu
* 20 to the Mem List at http://127.0.0.1:8000/mem

## Run native controller service on a separate terminal window
```sh
~/mycpu $ python controller.py
```
## View app at http://127.0.0.1:8000/home

## Alternatively, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
```sh
~/mycpu $ python manage.py runserver 0.0.0.0:8000
```
## Open a browser on another laptop and go to the server IP address
