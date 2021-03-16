# Lesson 5: Crossbar.io and Paho

* [Publish-subscribe](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
* [Web application messaging protocol](https://en.wikipedia.org/wiki/Web_Application_Messaging_Protocol) (WAMP)
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
* Run [cURL](https://en.wikipedia.org/wiki/CURL) to download data from [example.com](https://en.wikipedia.org/wiki/Example.com) with or without the progress meter
* Run Docker commands and hello-world
* Add pi to the Docker group as a non-root user, logout SSH, and reconnect SSH for this to take effect
```sh
$ man curl
$ curl example.com
$ curl -o example.txt example.com
$ cat example.txt
$ sudo docker version
$ sudo docker images
$ sudo docker run --rm hello-world
$ sudo docker images
$ sudo usermod -aG docker pi
$ logout
```
### Run Crossbar.io router on Terminal 1
```sh
$ git clone https://github.com/crossbario/crossbar-examples
$ cd crossbar-examples/getting-started
$ tree
$ docker pull crossbario/crossbar-armhf
$ docker run -v $PWD:/node -u 0 --rm --name=crossbar -it -p 8080:8080 crossbario/crossbar-armhf
```
* Open a browser and go to 192.168.x.xxx:8080/info (or 127.0.0.1:8080/info via VNC Viewer) to view the Crossbar.io node information
### Run publish-client on Terminal 2
```sh
$ sudo pip3 install -U autobahn[twisted,encryption,serialization,xbr]
$ cd crossbar-examples/getting-started
$ cd .crossbar
$ ls
$ cat config.json
$ cd ..
$ cd 1.hello-world
$ python3 client_component_publish.py
```
### Run subscribe-client on Terminal 3
```sh
$ cd crossbar-examples/getting-started/1.hello-world/
$ python3 client_component_subscribe.py
```
* Press control-c to stop subscribe-client > publish-client > router
## Lab 5B: Eclipse Mosquitto and Eclipse Paho

### Install and run Mosquitto to subscribe on one terminal and publish on another
```sh
$ sudo apt update
$ sudo apt install mosquitto mosquitto-clients
$ mosquitto_sub -h localhost -v -t "\$SYS/#"
```
* Press control-c to stop mosquitto_sub
```sh
$ service mosquitto status
$ netstat -tln
```
* [mqtt.eclipseprojects.io](https://mqtt.eclipseprojects.io/) is a public test MQTT broker service. It currently listens on the following ports:
  * 1883 : MQTT over unencrypted TCP
  * 8883 : MQTT over encrypted TCP
  * 80 : MQTT over unencrypted WebSockets (note: URL must be /mqtt )
  * 443 : MQTT over encrypted WebSockets (note: URL must be /mqtt )
* [Internet Assigned Numbers Authority](https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority) (IANA) [Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
  * 3306 : MySQL
  * 22 : SSH
  * 5900/5901/6001 : VNC
#### Terminal 1
```sh
$ mosquitto_sub -h localhost -v -t test/topic &
```
#### Terminal 2
```sh
$ mosquitto_pub -h localhost -t test/topic -m "Hello"
```
### Intall Paho and run code to subscribe on one terminal and publish on another
```sh
$ sudo pip3 install -U paho-mqtt
$ git clone https://github.com/eclipse/paho.mqtt.python.git
$ cd ~/iot/lesson5
$ python3 client.py
```
#### Terminal 1 (press control-c to stop)
```sh
$ python3 sub.py
```
#### Terminal 2
```sh
$ python3 pub.py
```
#### Terminal 1 (press control-c to stop)
```sh
$ python3 sub-multiple.py
```
#### Terminal 2
```sh
$ python3 pub-multiple.py
```
* Copy ~/iot/lesson5/system_info.py to ~/demo
* Copy ~/iot/lesson5/subraspi.py to ~/demo
* Copy ~/iot/lesson5/pubraspi.py to ~/demo
* Replace topic "Raspberry Pi" with a unique hostname in both subraspi.py and pubraspi.py
* Run subraspi.py on Terminal 1 and pubraspi.py on Terminal 2
#### Terminal 1 (press control-c to exit)
```sh
$ cd ~/demo
$ cp ~/iot/lesson5/subraspi.py .
$ nano subraspi.py
$ python3 subraspi.py
```
#### Terminal 2 on Raspberry Pi or another computer (press control-c to exit)
```sh
$ cd ~/demo
$ cp ~/iot/lesson5/system_info.py .
$ cp ~/iot/lesson5/pubraspi.py .
$ nano pubraspi.py
$ python3 pubraspi.py
```
