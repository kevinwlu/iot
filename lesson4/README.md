# <a href="https://goo.gl/bhktY0">Lesson 4</a>: Django and Flask

# Install Django and Django REST framework

pip3 -V

sudo pip3 install -U setuptools

sudo pip3 install -U django

sudo pip3 install -U djangorestframework

sudo pip3 install -U django-filter

sudo pip3 install -U markdown

sudo pip3 install -U requests

# Install MySQL server and client

sudo apt-get update

sudo apt-get install mysql-server mysql-client

sudo apt-get install python3-mysqldb

sudo mysql_secure_installation

# Install psutil (process and system utilities)

sudo pip3 install psutil

# Install Adafruit_Python_DHT library

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT

sudo python3 setup.py install

cd

# Install Adafruit_Python_BMP library

git clone https://github.com/adafruit/Adafruit_Python_BMP.git

cd Adafruit_Python_BMP

sudo python3 setup.py install

cd

# Install Flask-ask and Ngrok

sudo pip3 install -U flask-ask

sudo pip3 install 'cryptography<2.2'

sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip

sudo unzip ngrok-stable-linux-arm.zip

./ngrok http 5000

# Install Apache web server and PHP

sudo apt-get update

sudo apt-get install apache2

sudo service apache2 restart

sudo apt-get install php7.0

sudo service apache2 restart

# Build a Linux-Apache-MySQL-PHP (LAMP) web server with WordPress 

sudo apt-get install php7.0-mysql

cd /var/www/html

sudo chown pi: .

mv index.php index.php.bak

wget http://wordpress.org/latest.tar.gz

tar xzf latest.tar.gz

mv wordpress/* .

rm -rf wordpress latest.tar.gz

cd

mysql -u root -p

sudo service apache2 restart
