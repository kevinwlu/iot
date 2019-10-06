# <a href="https://goo.gl/shPybk">Lesson 5</a>: Crossbar.io and Paho

### Install Docker on a Raspberry Pi

curl -sSL get.docker.com | sh

### Add pi to the Docker Group as a non-root user (Control-d to logout and reconnect via SSH for this to take effect)

sudo usermod -aG docker pi

logout

### Run Docker images designed to work on ARM under the prefix armhf

docker run -it armhf/alpine /bin/sh

cat /etc/os-release

echo "Hi, this is a tiny Linux distribution!" | base64

echo "SGksIHRoaXMgaXMgYSB0aW55IExpbnV4IGRpc3RyaWJ1dGlvbiEK" | base64 -d

exit

docker run armhf/alpine date

### Build and run new image from Dockerfile

docker images

cp ~/iot/lesson9/Dockerfile ~/demo

cd ~/demo

docker build -t curl_docker .

docker run curl_docker

docker images

## Lab A: Install and run Crossbar.io to subscribe on one tab and publish on another

sudo apt-get install python3.pip python.dev libssl-dev

sudo pip3 install -U crossbar==18.4.1

sudo pip3 install -U autobahn==18.4.1

crossbar version

crossbar init --appdir hello

cd ~/hello/web

cp ~/iot/lesson5/favicon.ico .

cd ~/hello

crossbar start

crossbar stop

## Lab B: Install and run Mosquitto and Paho to subscribe on one terminal and publish on another

sudo apt-get install mosquitto mosquitto-clients

mosquitto_sub -h localhost -v -t "\\\$SYS/#"

### Press control-c to stop mosquitto_sub

mosquitto_sub -h localhost -v -t test/topic &

### Publish "Hello" on another terminal

mosquitto_pub -h localhost -t test/topic -m "Hello"

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
