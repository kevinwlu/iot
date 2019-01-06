# <a href="https://goo.gl/shPybk">Lesson 5</a>: Crossbar.io and Paho

# Crossbar.io

sudo pip3 install -U crossbar==18.4.1

crossbar version

crossbar init --appdir hello

cd ~/hello/web

cp ~/iot/lesson5/favicon.ico .

cd ~/hello

crossbar start

crossbar stop

# Mosquitto

sudo apt-get install mosquitto mosquitto-clients

mosquitto_sub -h localhost -v -t "\$SYS/#"

mosquitto_pub -h localhost -t test/topic -m "Hello"

mosquitto_sub -h localhost -v -t test/topic &

service mosquitto status

netstat -tln

sudo service mosquitto stop

# Install and run Paho to publish in one terminal and subscribe in another

sudo pip3 install -U paho-mqtt

git clone https://github.com/eclipse/paho.mqtt.python.git

cd ~/iot/lesson5

python3 client.py

python3 sub.py

python3 pub.py

python3 sub-multiple.py

python3 pub-multiple.py

python3 subraspi.py

python3 pubraspi.py

# AWS CLI

sudo pip3 install -U awscli
