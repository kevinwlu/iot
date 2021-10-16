# Lesson 4: Django and Flask

* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
  * [Django Reinhardt](https://en.wikipedia.org/wiki/Django_Reinhardt)
  * [Django Software Foundation](https://en.wikipedia.org/wiki/Django_Software_Foundation)
  * [Django's Structure - A Heretic’s Eye View](https://djangobook.com/mdj2-django-structure/) by [The Django Book](https://djangobook.com/)
* [Representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer) (REST)
  * [Django REST framework](https://www.django-rest-framework.org/)
* [Databases](https://docs.djangoproject.com/en/3.2/ref/databases/)
  * [MariaDB](https://en.wikipedia.org/wiki/MariaDB)
  * [MySQL](https://en.wikipedia.org/wiki/MySQL)
  * [SQLite](https://en.wikipedia.org/wiki/SQLite)
  * [Firebase](https://en.wikipedia.org/wiki/Firebase)
  * [How to use Firebase with Django project](https://medium.com/@canadiyaman/how-to-use-firebase-with-django-project-34578516bafe) by [Can Adiyaman](https://github.com/canadiyaman)
  * [CockroachDB](https://en.wikipedia.org/wiki/CockroachDB)
  * [Build a Python app with CockroachDB and Django](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-django.html)
* [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
* [ngrok](https://ngrok.com/)
  * [Repository](https://github.com/inconshreveable/ngrok)
  * [Grok](https://en.wikipedia.org/wiki/Grok)
  * [Jargon File](https://en.wikipedia.org/wiki/Jargon_File)
* [LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)) (Linux, Apache, MySQL, PHP)
  * [WordPress](https://en.wikipedia.org/wiki/WordPress)
* [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) (WWW)
  * [Web 2.0](https://en.wikipedia.org/wiki/Web_2.0)
  * [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web)
* [Uniform Resource Locator](https://en.wikipedia.org/wiki/URL) (URL)
* [Hypertext Markup Language](https://en.wikipedia.org/wiki/HTML) (HTML)
* [Cascading Style Sheets](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) (CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) (JS)
* [Application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (API)
* [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) (IETF)
  * [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (HTTP)
  * [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
  * [Hypertext Transfer Protocol Secure](https://en.wikipedia.org/wiki/HTTPS) (HTTPS)
  * [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS)
* [Apache Software Foundation](https://en.wikipedia.org/wiki/The_Apache_Software_Foundation)
* [LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)) (Linux, Apache, MySQL, PHP/Perl/Python)

## Labs 4A and 4B: Django and Django REST

### Install Django and Django REST framework on Raspberry Pi
```sh
$ pip3 -V
$ pip3 list
$ sudo pip3 install -U setuptools
$ sudo pip3 install -U django
$ sudo pip3 install -U djangorestframework
$ sudo pip3 install -U django-filter
$ sudo pip3 install -U markdown
$ sudo pip3 install -U requests
```
### Install MariaDB server and client on Raspberry Pi
### By default, Django uses [SQLite](https://en.wikipedia.org/wiki/SQLite)
```sh
$ sudo apt update
$ sudo apt install mariadb-server mariadb-client
$ sudo apt install python3-mysqldb
$ sudo pip3 install -U mysqlclient
$ sudo mysql_secure_installation
Enter current password for root (enter for none): 
Set root password? [Y/n] 
New password: PASSWORD
Re-enter new password: PASSWORD
Remove anonymous users? [Y/n] 
Disallow root login remotely? [Y/n] 
Remove test database and access to it? [Y/n] 
Reload privilege tables now? [Y/n] 
```
### Start Django project [stevens](https://github.com/kevinwlu/iot/tree/master/lesson4/stevens)
### Start Dhango REST project [mycpu](https://github.com/kevinwlu/iot/tree/master/lesson4/mycpu)
### Start Django REST project [myraspi](https://github.com/kevinwlu/iot/tree/master/lesson4/myraspi) on Raspberry Pi
### Start four Django REST projects on Raspberry Pi with sensors
1. [weather](https://github.com/kevinwlu/iot/tree/master/lesson4/weather)
2. [lighting](https://github.com/kevinwlu/iot/tree/master/lesson4/lighting)
3. [parking](https://github.com/kevinwlu/iot/tree/master/lesson4/parking)
4. [sensing](https://github.com/kevinwlu/iot/tree/master/lesson4/sensing)

## Lab 4C: Flask

### Run Flask server and open a browser via VNC Viewer and go to http://127.0.0.1:5000/
```sh
$ cd ~/iot/lesson4
python3 hello_world.py
```
### Terminal 1 on Raspberry Pi: Install [Flask-Ask](https://github.com/johnwheeler/flask-ask) and [Ngrok](https://ngrok.com/) for Alexa Skill Kit (ASK)
```sh
$ sudo pip3 install -U flask-ask
$ sudo pip3 install 'cryptography<2.2'
$ sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
$ sudo unzip ngrok-stable-linux-arm.zip
$ ./ngrok http 5000
```
### Terminal 2 on Raspberry Pi: [Memory Game](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development)
```sh
$ cd ~/iot/lesson4
$ python3 memory_game.py
```
### Open a browser and sign in [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask)
* Click "Create Skill" > Enter Skill name in title case: Memory Game > 1. Choose a model: Custom (SELECTED) > 2. Choose a host: Provision your own (SELECTED) > Click "Create skill" > Choose a template: Hello World Skill > Click "Choose"
* Invocation > Enter Skill Invocation Name in lowercase: memory game
* Interaction Model > 
  * JSON Editor > Replace all intent schema and sample utterances by copying and pasting the entire content of ~/iot/lesson4/memory_game.json
  * Save Model > Build Model
* Endpoint >
  * Service Endpoint Type: HTTPS
  * Default Region: https://xxxxxxxxxxxx.ngrok.io (copy and paste the endpoint provided by Ngrok)
  * Select "My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority"
  * Save Endpoints
* Click "Test" tab > Enable skill testing from "Off" to "Development"
  * Type or click and hold the microphone button to speak
  * "memory game"
    
    Alexa: "Welcome to memory game. I'm going to say three numbers for you to repeat backwards. Ready?"
  * "yes"
    
    Alexa: "Can you repeat the numbers 0, 9, 6 backwards?"
  * "six nine zero"
    
    Alexa: "Good job!"

## Lab 4D: LAMP

### On Raspberry Pi, install [Apache HTTP server](https://en.wikipedia.org/wiki/Apache_HTTP_Server) and [PHP](https://en.wikipedia.org/wiki/PHP)
```sh
$ sudo apt update
$ sudo apt install apache2
$ sudo service apache2 restart
```
### Open a Chromium browser and go to http://127.0.0.1, i.e., [localhost](https://en.wikipedia.org/wiki/Localhost), to view the Apache2 Debian Default Page
```sh
$ sudo apt install php7.3
$ cd /var/www/html
$ ls
$ sudo mv index.html index.html.bak
$ sudo cp ~/iot/lesson4/index.php .
$ sudo service apache2 restart
```
### Open a Chromium browser and go to http://127.0.0.1 to view "Hello world!" and the PHP info

### Build a Linux-Apache-MySQL-PHP (LAMP) web server with [WordPress](https://en.wikipedia.org/wiki/WordPress)
```sh
$ sudo apt install php7.3-mysql
$ cd /var/www/html
$ sudo chown pi: .
$ mv index.php index.php.bak
$ wget http://wordpress.org/latest.tar.gz
$ tar xzf latest.tar.gz
$ mv wordpress/* .
$ rm -rf wordpress latest.tar.gz
$ cd
```
### Create database and grant all privileges
```sh
$ sudo mysql -u root -p
```
Enter password: PASSWORD

MariaDB [(none)]> use mysql

MariaDB [mysql]> create database wordpress;

MariaDB [mysql]> grant all privileges on wordpress.* to pi@localhost;

MariaDB [mysql]> quit
```sh
$ sudo service apache2 restart
```
### Open a Chromium browser and go to http://127.0.0.1 to configure Wordpress
```sh
$ nano wp-config.php
```
### Copy the highlighted text, paste it, save wp-config.php, and run the installation
