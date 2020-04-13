# <a href="https://goo.gl/RIzzfl">Lesson 9</a>: NETCONF and YANG

## Lab: <a href="https://en.wikipedia.org/wiki/YANG">YANG</a>

### Install and run <a href="https://github.com/mbj4668/pyang">pyang</a> on a Raspberry Pi
```sh
$ sudo apt install libxml2-dev libxslt1-dev
$ sudo pip3 install -U lxml pyang
$ cp ~/iot/lesson9/intrusiondetection.yang ~/demo
$ cd ~/demo
$ pyang -f yin -o intrusiondetection.yin intrusiondetection.yang
$ pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef
```
### Install <a href="https://en.wikipedia.org/wiki/PlantUML">PlantUML</a> on a laptop or Raspberry Pi
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
$ sudo apt update
$ sudo apt install gimp pinta
$ cd ~/demo
$ pinta intrusiondetection.png
$ gimp -h
$ gimp -a intrusiondetection.png
```
