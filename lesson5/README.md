# <a href="https://goo.gl/shPybk">Lesson 5</a>: Crossbar.io and Paho

# Crossbar.io

sudo pip3 install -U crossbar

crossbar version

crossbar init --appdir hello

# Mosquitto

sudo apt-get install mosquitto mosquitto-clients

mosquitto_sub -h localhost -v -t "\$SYS/#"

mosquitto_pub -h localhost -t test/topic -m "Hello"

mosquitto_sub -h localhost -v -t test/topic &

service mosquitto status

netstat -tln

sudo service mosquitto stop

# Paho

sudo pip3 install -U paho-mqtt

git clone https://github.com/eclipse/paho.mqtt.python.git

# AWS CLI

sudo pip3 install -U awscli
