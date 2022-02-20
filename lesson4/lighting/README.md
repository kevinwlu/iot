# Django REST Project "Lighting" on Raspberry Pi

This project requires a light-dependent resistor (LDR), light-emitting diode (LED), 1kΩ and 10kΩ resistors, 
[MCP3008](https://www.adafruit.com/product/856) analog-to-digital converter (ADC), and if desired, [SRD-05VDC-SL-C](https://www.parallax.com/product/single-relay-board/) relay with a light bulb

![ldr-led_bb.png](/lesson4/lighting/ldr-led_bb.png)

## Start a Django project
```sh
pi@raspberrypi:~ $ django-admin startproject lighting
pi@raspberrypi:~ $ cd lighting
pi@raspberrypi:~/lighting $ ls
lighting  manage.py 
```
## Start a Django app
```sh
pi@raspberrypi:~/lighting $ python3 manage.py startapp myapp
pi@raspberrypi:~/lighting $ ls
lighting  manage.py  myapp  
```
## Edit settings.py in ~/lighting/lighting

* Follow ~/iot/lesson4/lighting/settings.txt

```sh
pi@raspberrypi:~/lighting $ cd lighting
pi@raspberrypi:~/lighting/lighting $ ls
asgi.py  __init__.py  __pycache__  settings.py  urls.py  wsgi.py
pi@raspberrypi:~/lighting/lighting $ nano settings.py
```
## Copy urls.py to ~/lighting/lighting
```sh
pi@raspberrypi:~/lighting/lighting $ cp ~/iot/lesson4/lighting/urls.py .
pi@raspberrypi:~/lighting/lighting $ cd ..
```
## Copy models.py, views.py, and serializers.py to ~/lighting/myapp
```sh
pi@raspberrypi:~/lighting $ cd myapp
pi@raspberrypi:~/lighting/myapp $ ls
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
pi@raspberrypi:~/lighting/myapp $ cp ~/iot/lesson4/lighting/models.py .
pi@raspberrypi:~/lighting/myapp $ cp ~/iot/lesson4/lighting/views.py .
pi@raspberrypi:~/lighting/myapp $ cp ~/iot/lesson4/lighting/serializers.py .
```
## Change the default password 'raspberry' in views.py
```sh
pi@raspberrypi:~/lighting/myapp $ nano views.py
```
## Copy index.html
```sh
pi@raspberrypi:~/lighting/myapp $ mkdir static templates
pi@raspberrypi:~/lighting/myapp $ cd templates
pi@raspberrypi:~/lighting/myapp/templates $ mkdir myapp
pi@raspberrypi:~/lighting/myapp/templates $ cd myapp
pi@raspberrypi:~/lighting/myapp/templates/myapp $ cp ~/iot/lesson4/lighting/index.html .
```
## Copy static files
```sh
pi@raspberrypi:~/lighting/myapp/templates/myapp $ cd ~/lighting/myapp/static
pi@raspberrypi:~/lighting/myapp/static $ cp ~/iot/lesson4/static/favicon.ico .
pi@raspberrypi:~/lighting/myapp/static $ cd ~/lighting
```
## Copy controller.py to ~/lighting
```sh
pi@raspberrypi:~/lighting $ cp ~/iot/lesson4/lighting/controller.py .
```
## After the first time, skip these three steps if no changes
* The superuser PASSWORD shall be the same as the one in views.py
```sh
pi@raspberrypi:~/lighting $ python3 manage.py makemigrations myapp
pi@raspberrypi:~/lighting $ python3 manage.py migrate
pi@raspberrypi:~/lighting $ python3 manage.py createsuperuser
Username (leave blank to use 'pi'):
Email address: EMAIL_ADDRESS
Password: PASSWORD
Password (again): PASSWORD
Superuser created successfully.
```
## Terminal 1: Run Django server
```sh
pi@raspberrypi:~/lighting $ python3 manage.py runserver
```
## Open the Chromium browser on Raspberry Pi via VNC Viewer

## At the first time, post the following in HTML form:

* auto to the state list at http://127.0.0.1:8000/mode
* off to the state list at http://127.0.0.1:8000/state

## Terminal 2: Run native controller service
```sh
pi@raspberrypi:~/lighting $ python3 controller.py
```
## View app at http://127.0.0.1:8000/home

## Alternatively, run Django server at [0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0):8000
```sh
pi@raspberrypi:~/lighting $ python3 manage.py runserver 0.0.0.0:8000
```
## Open a laptop browser and go to the Raspbbery Pi IP address as opposed to the localhost
![lighting.png](/lesson4/lighting/lighting.png)
