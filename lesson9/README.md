# <a href="https://goo.gl/RIzzfl">Lesson 9</a>: NETCONF and YANG

## Lab: YANG

### Install and run pyang on a Raspberry Pi
```sh
$ sudo apt-get install libxml2-dev libxslt1-dev
$ sudo pip3 install -U lxml pyang
$ cp ~/iot/lesson9/intrusiondetection.yang ~/demo
$ cd demo
$ pyang -f yin -o intrusiondetection.yin intrusiondetection.yang
$ pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef
```
### Install PlantUML on a laptop or Raspberry Pi
```sh
$ sudo pip3 install -U plantuml
```
### Run PlantUML to create a sequence diagram in PNG
```sh
$ python3 -m plantuml intrusiondetection.uml
```
### Install and run GIMP and Pinta to display a PNG file

#### Alternatives to VNC Viewer

#### On macOS with XQuartz, run SSH -Y to enable X11 forwarding

#### On Windows, run Xming then PuTTY with SSH and X11 forwarding
```sh
$ cd
$ sudo apt-get update
$ sudo apt-get install gimp pinta
$ cd demo
$ pinta intrusiondetection.png
$ gimp -h
$ gimp -a intrusiondetection.png
```
