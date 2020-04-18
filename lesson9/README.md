# [Lesson 9](https://goo.gl/RIzzfl): NETCONF and YANG

## Lab: [YANG](https://en.wikipedia.org/wiki/YANG)

### Install and run [pyang](https://github.com/mbj4668/pyang) on a Raspberry Pi
```sh
$ sudo apt install libxml2-dev libxslt1-dev
$ sudo pip3 install -U lxml pyang
$ cp ~/iot/lesson9/intrusiondetection.yang ~/demo
$ cd ~/demo
$ pyang -f yin -o intrusiondetection.yin intrusiondetection.yang
$ pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef
```
### Install [PlantUML](https://en.wikipedia.org/wiki/PlantUML) on a laptop or Raspberry Pi
```sh
$ sudo pip3 install -U plantuml
```
### Run PlantUML to create a sequence diagram in <a href="https://en.wikipedia.org/wiki/Portable_Network_Graphics">PNG</a>
```sh
$ python3 -m plantuml intrusiondetection.uml
```
### Install and run [GIMP](https://en.wikipedia.org/wiki/GIMP) and [Pinta](https://en.wikipedia.org/wiki/Pinta_(software)) to display a PNG file

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

## Bonus Lab: [Qiskit](https://en.wikipedia.org/wiki/Qiskit)

### Install qiskit on a laptop and run example code

```sh
$ sudo pip3 install qiskit
$ sudo pip3 install qiskit-terra[visualization]
$ cd ~/iot/lesson9
$ python3 qiskit_terra_example.py
$ python3 qiskit_aqua_example.py
$ python3 qiskit_aer_example.py
$ python3 qiskit_ignis_example.py
```
