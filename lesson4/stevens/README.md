pi@raspberrypi:~ $ django-admin startproject stevens

pi@raspberrypi:~ $ cd stevens

pi@raspberrypi:~/stevens $ ls

manage.py  stevens

pi@raspberrypi:~/stevens $ python manage.py startapp myapp

pi@raspberrypi:~/stevens $ ls

manage.py  myapp  stevens

pi@raspberrypi:~/stevens $ cd stevens

pi@raspberrypi:~/stevens/stevens $ ls

__init__.py  __init__.pyc  settings.py  settings.pyc  urls.py  wsgi.py

pi@raspberrypi:~/stevens/stevens $ cd ..

pi@raspberrypi:~/stevens $ cd myapp

pi@raspberrypi:~/stevens/myapp $ ls

admin.py   apps.py  __init__.py  migrations  models.py  tests.py  views.py

pi@raspberrypi:~/stevens/myapp $ mkdir static templates

pi@raspberrypi:~/stevens/myapp $ ls

admin.py  __init__.py  models.py  templates  views.py

apps.py   migrations   static     tests.py

pi@raspberrypi:~/stevens/myapp $ cd templates

pi@raspberrypi:~/stevens/myapp/templates $ mkdir myapp

pi@raspberrypi:~/stevens/myapp/templates $ cd myapp

pi@raspberrypi:~/stevens/myapp/templates/myapp $ ls

index.html

pi@raspberrypi:~/stevens/myapp/templates/myapp $ cd ~/stevens/myapp/static

pi@raspberrypi:~/stevens/myapp/static $ mkdir myapp

pi@raspberrypi:~/stevens/myapp/static $ cd myapp

pi@raspberrypi:~/stevens/myapp/static/myapp $ ls

bootstrap.min.css  bootstrap.min.js  favicon.ico  jquery.min.js  script.js

pi@raspberrypi:~/stevens/myapp/static/myapp $ cd ~/stevens

# After the first time, skip these three steps if no changes

pi@raspberrypi:~/stevens $ python manage.py makemigrations myapp

pi@raspberrypi:~/stevens $ python manage.py migrate

pi@raspberrypi:~/stevens $ python manage.py createsuperuser

Username (leave blank to use 'pi'): <username>

Email address: <email address>

Password: <password>

Password (again): <password>

Superuser created successfully.

pi@raspberrypi:~/stevens $ python manage.py runserver

# Add or change (not delete) temperature data at

# http://127.0.0.1:8000/admin/

# View app from a browser at http://127.0.0.1:8000/
