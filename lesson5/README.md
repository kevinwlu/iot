# Lesson 5: MQTT and Paho
* [Publish-subscribe](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) (Pub/Sub)
* [Message queuing telemetry transport](https://en.wikipedia.org/wiki/MQTT) (MQTT)
  * [What is MQTT](https://www.youtube.com/watch?v=t5b7gGYAezQ) by [IoT for All](https://www.youtube.com/@IoTForAll)
  * [Roger Light](https://github.com/ralight)
    * [Cedalo](https://cedalo.com/) 
    * [GmbH](https://en.wikipedia.org/wiki/Gesellschaft_mit_beschr%C3%A4nkter_Haftung)
    * [AG](https://en.wikipedia.org/wiki/Aktiengesellschaft)
  * [OASIS](https://en.wikipedia.org/wiki/OASIS_(organization)) (Organization for the Advancement of Structured Information Standards)
  * [MQTT specification](https://mqtt.org/mqtt-specification/)
  * [Comparison of MQTT implementations](https://en.wikipedia.org/wiki/Comparison_of_MQTT_implementations)
  * [Eclipse Foundation](https://en.wikipedia.org/wiki/Eclipse_Foundation)
  * [Eclipse Mosquitto](https://mosquitto.org/)
  * [Eclipse Paho](https://en.wikipedia.org/wiki/Eclipse_Paho)
  * [Eclipse IoT Sandboxes](https://iot.eclipse.org/projects/sandboxes/)
  * [Sandbox (software development)](https://en.wikipedia.org/wiki/Sandbox_(software_development))
  * [Sandbox (computer security)](https://en.wikipedia.org/wiki/Sandbox_(computer_security))
  * [Eclipse Paho](https://en.wikipedia.org/wiki/Eclipse_Paho)
    * [Paho](https://wiki.eclipse.org/Paho) in Eclipse Wiki
    * [Paho](https://www.merriam-webster.com/dictionary/paho) is a [Hopi](https://en.wikipedia.org/wiki/Hopi) plumed prayer stick
      * [Susanne Page](https://en.wikipedia.org/wiki/Susanne_Page) 1938&mdash;2024 was a photographer known for her photos of [indigenous peoples](https://en.wikipedia.org/wiki/Indigenous_peoples) of the [Southwestern United States](https://en.wikipedia.org/wiki/Southwestern_United_States)
    * [Paho](https://maoridictionary.co.nz/search/?keywords=paho) in Te Aka Maori Dictionary
      * (Verb) to broadcast, make widely known, announce, disseminate, transmit
      * [Maori people](https://en.wikipedia.org/wiki/M%C4%81ori_people)
    * [Paho](https://forvo.com/search/paho/) in [Minangkabau language](https://en.wikipedia.org/wiki/Minangkabau_language)
    * [Paho](https://en.wikipedia.org/wiki/Paho) is also a village in Khiron block of Rae Bareli district, Uttar Pradesh, India
* [Web application messaging protocol](https://en.wikipedia.org/wiki/Web_Application_Messaging_Protocol) (WAMP)
  * [WAMP specification](https://wamp-proto.org/spec.html)
  * [cURL](https://en.wikipedia.org/wiki/CURL) (Client URL)
  * [Docker](https://en.wikipedia.org/wiki/Docker_(software))
  * [List of Linux containers](https://en.wikipedia.org/wiki/List_of_Linux_containers)
  * [ARM architecture](https://en.wikipedia.org/wiki/ARM_architecture)
  * ARM [hard float](https://www.raspberrypi.org/forums/viewtopic.php?t=11177) (armhf)
  * [Crossbar.io](https://crossbar.io/docs/Getting-Started/)
  * [Crossbar switch](https://en.wikipedia.org/wiki/Crossbar_switch)

## Lab 5A: Eclipse Mosquitto and Eclipse Paho

### On Windows, [download](https://mosquitto.org/download/) and install Mosquitto
* Go to System Properties > Environment Variables > Path > New, and enter C:\Program Files\Mosquitto
### On macOS, install and start Mosquitto with
```sh
brew install mosquitto
brew services start mosquitto
```
### On Raspberry Pi, install and run Mosquitto to subscribe on one terminal and publish on another
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
* [paho-mqtt-2.0.0 client issue](https://github.com/eclipse/paho.mqtt.python/issues/814)
* Breaking change warning: [paho.mqtt.python](https://github.com/eclipse/paho.mqtt.python)
  * [Release notes](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html)
  * [Migrations](https://eclipse.dev/paho/files/paho.mqtt.python/html/migrations.html)
```sh
$ sudo pip3 install paho-mqtt
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
#### Terminal 1 (press control-c to stop)
```sh
$ python3 subcpu.py
```
#### Terminal 2
```sh
$ python3 pubcpu.py
```
### On older versions of Raspberry Pi OS before Bullseye, change /usr/bin/vcgencmd to /opt/vc/bin/vcgencmd in system_info.py
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

## Optional Lab 5B: Crossbar.io

### [Docker Get Started](https://www.docker.com/get-started) includes

* Docker Desktop download for [macOS](https://docs.docker.com/docker-for-mac/install/) or [Windows](https://docs.docker.com/docker-for-windows/install/)
* Docker Engine for [Linux](https://docs.docker.com/engine/install/) (CentOS, Debian, Fedora, Raspberry Pi OS, and Ubuntu)
```sh
$ docker version
$ docker images
$ docker 
$ docker run --rm hello-world
$ docker run -it ubuntu bash
# pwd
# ls
# cat /etc/os-release
# date
# exit
```

### On Raspberry Pi, install Docker
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
### Run Crossbar.io router on Raspberry Pi Terminal 1
```sh
$ git clone https://github.com/crossbario/crossbar-examples
$ cd crossbar-examples/getting-started
$ tree
$ docker pull crossbario/crossbar-armhf
$ docker run -v $PWD:/node -u 0 --rm --name=crossbar -it -p 8080:8080 crossbario/crossbar-armhf
```
* Open a browser and go to 192.168.x.xxx:8080/info (or 127.0.0.1:8080/info via VNC Viewer) to view the Crossbar.io node information
### Run publish-client on Raspberry Pi Terminal 2
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
### Run subscribe-client on Raspberry Pi Terminal 3
```sh
$ cd crossbar-examples/getting-started/1.hello-world/
$ python3 client_component_subscribe.py
```
* Press control-c to stop subscribe-client > publish-client > router
