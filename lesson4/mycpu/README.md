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
* Follow ~/iot/lesson4/xidian/settings.txt
```sh
~/mycpu $ cd myraspi
~/mycpu/mycpu $ nano settings.py
```
## Copy urls.py to ~/myraspi/myraspi
```sh
~/mycpu/mycpu $ cp ~/iot/lesson4/myraspi/urls.py .
~/mycpu/mycpu $ cd ..
```
## Copy admin.py, models.py, views.py, and serializers.py to ~/mycpu/myapp
```sh
~/mycpu $ cd myapp
~/mycpu/myapp $ cp ~/iot/lesson4/myraspi/admin.py .
~/mycpu/myapp $ cp ~/iot/lesson4/myraspi/models.py .
~/mycpu/myapp $ cp ~/iot/lesson4/myraspi/views.py .
~/mycpu/myapp $ cp ~/iot/lesson4/myraspi/serializers.py .
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
~/mycpu/myapp/templates/myapp $ cp ~/iot/lesson4/myraspi/index.html .
```
## Edit index.html to add the Google Maps API key
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
## Copy system_info.py and controller.py to ~/myraspi
* system_info.py only runs on Raspberry Pi
* On Windows or macOS, replace CPU temperature with other [psutil](https://pypi.org/project/psutil/) information
```sh
~/mycpu $ cp ~/iot/lesson4/myraspi/controller.py .
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
Password: PASSWORD
Password (again): PASSWORD
Superuser created successfully.
```
## Run Django server
```sh
~/mycpu $ python manage.py runserver
```
## Open a browser

### At the first time, go to http://127.0.0.1:8000/admin

### Login with Django administration username (admin) and PASSWORD

### Click location data to add 

* Location Xidian

* Latitude 34.12250

* Longitude 108.84029

### Click SAVE

### Post the following in HTML form:

* 2021 to the Dt List at http://127.0.0.1:8000/dt

* 50 to the Tmp List at http://127.0.0.1:8000/tmp

* 20 to the Cpu List at http://127.0.0.1:8000/cpu

## Run native controller service on a separate terminal window
```sh
~/mycpu $ python3 controller.py
```
## View app at http://127.0.0.1:8000/home

## Alternatively, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
```sh
~/mycpu $ python3 manage.py runserver 0.0.0.0:8000
```
## Open a browser on another laptop and go to the server IP address
