# Lesson 5: Crossbar.io and Paho

* [Publish-subscribe](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
* [Web application messaging protocol](https://en.wikipedia.org/wiki/Web_Application_Messaging_Protocol) (WAMP)
* [cURL](https://en.wikipedia.org/wiki/CURL)
* [example.com](https://en.wikipedia.org/wiki/Example.com)
* [Docker](https://en.wikipedia.org/wiki/Docker_(software))
* [Crossbar.io](https://crossbar.io/docs/Getting-Started/)
* [Message queuing telemetry transport](https://en.wikipedia.org/wiki/MQTT) (MQTT)
* [Eclipse Foundation](https://en.wikipedia.org/wiki/Eclipse_Foundation)
* [Eclipse Mosquitto](https://mosquitto.org/)
* [Eclipse Paho](https://en.wikipedia.org/wiki/Eclipse_Paho)

## Lab 5A: Crossbar.io

### Install Docker on Raspberry Pi OS
* [Docker Get Started](https://www.docker.com/get-started) includes Docker Desktop download for Mac or Windows and Docker Engine for Linux (Fedora, CentOS, AWS, Azure, Ubuntu, Debian)
* Install Docker on Raspberry Pi OS by following these [instructions](https://withblue.ink/2020/06/24/docker-and-docker-compose-on-raspberry-pi-os.html)
```sh
$ sudo docker version
$ sudo docker images
$ sudo docker run --rm hello-world
$ sudo docker images
```
### Run Crossbar.io router on Terminal 1
```sh
$ git clone https://github.com/crossbario/crossbar-examples
$ cd crossbar-examples/getting-started
$ docker pull crossbario/crossbar-armhf
$ docker run -v $PWD:/node -u 0 --rm --name=crossbar -it -p 8080:8080 crossbario/crossbar-armhf
```
* Open a browser and go to 192.168.x.xxx:8080/info (or 127.0.0.1:8080/info via VNC Viewer) to see the Crossbar.io router status
### Run publish-client on Terminal 2
```sh
$ sudo pip3 install -U autobahn[twisted,encryption,serialization,xbr]
$ cd crossbar-examples/getting-started/1.hello-world/
$ python3 client_component_publish.py
```
### Run subscribe-client on Terminal 3
```sh
$ cd crossbar-examples/getting-started/1.hello-world/
$ python3 client_component_subscribe.py
```
* Enter control-c to exit in the reverse order, i.e., subscribe-client > publish-client > router
## Lab 5B: Eclipse Mosquitto and Eclipse Paho

### Install and run Mosquitto and Paho to subscribe on one terminal and publish on another
```sh
$ sudo apt install mosquitto mosquitto-clients
$ mosquitto_sub -h localhost -v -t "\$SYS/#"
```
### Press control-c to stop mosquitto_sub
```sh
$ mosquitto_sub -h localhost -v -t test/topic &
```
### Publish "Hello" on another terminal
```sh
$ mosquitto_pub -h localhost -t test/topic -m "Hello"
$ service mosquitto status
$ netstat -tln
$ sudo pip3 install -U paho-mqtt
$ git clone https://github.com/eclipse/paho.mqtt.python.git
$ cd ~/iot/lesson5
$ python3 client.py
```
#### Terminal 1 (control-c to exit)
```sh
$ python3 sub.py
```
#### Terminal 2 on the same or another Raspberry Pi
```sh
$ python3 pub.py
```
#### Terminal 1 (control-c to exit)
```sh
$ python3 sub-multiple.py
```
#### Terminal 2 on the same or another Raspberry Pi
```sh
$ python3 pub-multiple.py
```
#### Terminal 1 (control-c to exit)
```sh
python3 subraspi.py
```
#### Terminal 2 on the same or another Raspberry Pi
```sh
python3 pubraspi.py
```
