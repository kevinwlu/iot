# <a href="https://goo.gl/shPybk">Lesson 5</a>: Crossbar.io and Paho

# Lab A: Install and run Crossbar.io publish on one tab and subscribe on another

sudo pip3 install -U crossbar==18.4.1

crossbar version

crossbar init --appdir hello

cd ~/hello/web

cp ~/iot/lesson5/favicon.ico .

cd ~/hello

crossbar start

crossbar stop

# Lab B: Install and run Mosquitto and Paho to publish on one terminal and subscribe on another

sudo apt-get install mosquitto mosquitto-clients

mosquitto_sub -h localhost -v -t "\$SYS/#"

mosquitto_pub -h localhost -t test/topic -m "Hello"

mosquitto_sub -h localhost -v -t test/topic &

service mosquitto status

netstat -tln

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
