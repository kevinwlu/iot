# Start a Django project

pi@raspberrypi:~ $ django-admin startproject stevens

pi@raspberrypi:~ $ cd stevens

pi@raspberrypi:~/stevens $ ls

manage.py  stevens

# Start a Django app

pi@raspberrypi:~/stevens $ python3 manage.py startapp myapp

pi@raspberrypi:~/stevens $ ls

manage.py  myapp  stevens

# Create MySQL database

pi@raspberrypi:~ $ mysql -u root -p

Enter password: <PASSWORD>

mysql> create database stevens;

mysql> quit

# Edit settings.py and urls.py in ~/stevens/stevens

# Remember to change PASSWORD in settings.py

pi@raspberrypi:~/stevens $ cd stevens

pi@raspberrypi:~/stevens/stevens $ nano settings.py

pi@raspberrypi:~/stevens/stevens $ nano urls.py

pi@raspberrypi:~/stevens/stevens $ cd ..

# Edit admin.py, models. py, and views.py in ~/stevens/myapp

pi@raspberrypi:~/stevens $ cd myapp

pi@raspberrypi:~/stevens/myapp $ nano admin.py

pi@raspberrypi:~/stevens/myapp $ nano models.py

pi@raspberrypi:~/stevens/myapp $ nano views.py

# Copy index.html and static files

pi@raspberrypi:~/stevens/myapp $ mkdir static templates

pi@raspberrypi:~/stevens/myapp $ cd templates

pi@raspberrypi:~/stevens/myapp/templates $ mkdir myapp

pi@raspberrypi:~/stevens/myapp/templates $ cd myapp

pi@raspberrypi:~/stevens/myapp/templates/myapp $ cp ~/iot/lesson4/stevens/index.html .

pi@raspberrypi:~/stevens/myapp/templates/myapp $ cd ~/stevens/myapp/static

pi@raspberrypi:~/stevens/myapp/static $ cp ~/iot/lesson4/stevens/favicon.ico .

pi@raspberrypi:~/stevens/myapp/static $ mkdir myapp

pi@raspberrypi:~/stevens/myapp/static $ cd myapp

pi@raspberrypi:~/stevens/myapp/static/myapp $ cp ~/iot/lesson4/stevens/*css .

pi@raspberrypi:~/stevens/myapp/static/myapp $ cp ~/iot/lesson4/stevens/*js .

pi@raspberrypi:~/stevens/myapp/static/myapp $ cd ~/stevens

# After the first time, skip these three steps if no changes

pi@raspberrypi:~/stevens $ python3 manage.py makemigrations myapp

pi@raspberrypi:~/stevens $ python3 manage.py migrate

pi@raspberrypi:~/stevens $ python3 manage.py createsuperuser

Username (leave blank to use 'pi'): <username>

Email address: <email address>

Password: <password>

Password (again): <password>

Superuser created successfully.

pi@raspberrypi:~/stevens $ python3 manage.py runserver

# Add or change (not delete) temperature data at

# http://127.0.0.1:8000/admin/

# View app from a browser at http://127.0.0.1:8000/
