# Lesson 9: NETCONF and YANG
* [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
* [YANG](https://en.wikipedia.org/wiki/YANG)
* [PlantUML](https://en.wikipedia.org/wiki/PlantUML)
* [GIMP](https://en.wikipedia.org/wiki/GIMP)
* [Pinta](https://en.wikipedia.org/wiki/Pinta_(software))
* [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)
* [Qiskit](https://en.wikipedia.org/wiki/Qiskit)
* [Cloud Native Computing Foundation](https://en.wikipedia.org/wiki/Cloud_Native_Computing_Foundation) (CNCF)
* [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) (K8s)

## Lab 9A: YANG ([Yet Another](https://en.wikipedia.org/wiki/Yet_another) Next Generation)

### Install and run [pyang](https://github.com/mbj4668/pyang) on a Raspberry Pi
```sh
$ sudo apt install libxml2-dev libxslt1-dev
$ sudo pip3 install -U lxml pyang
$ cp ~/iot/lesson9/intrusiondetection.yang ~/demo
$ cd ~/demo
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
### Install and run GIMP and Pinta to display a PNG file via VNC Viewer
* Alternativly, run SSH -Y to enable X11 forwarding on macOS with XQuartz or on Windows with Xming
```sh
$ cd
$ sudo apt update
$ sudo apt install gimp pinta
$ cd ~/demo
$ pinta intrusiondetection.png
$ gimp -h
$ gimp -a intrusiondetection.png
```

## Lab 9B: Qiskit

### Install qiskit on a laptop (not Raspberry Pi), create an [IBM Quantum Experience account](https://quantum-computing.ibm.com/), copy API token from [account](https://quantum-computing.ibm.com/account), and save API token

```sh
$ sudo pip3 install qiskit
$ sudo pip3 install qiskit-terra[visualization]
$ python3
>>> from qiskit import IBMQ
>>> IBMQ.save_account('MY_API_TOKEN')
>>> exit()
```

### Run examples of Qiskit

```sh
$ cd ~/iot/lesson9
$ python3 qiskit_terra_example.py
$ python3 qiskit_aer_example.py
$ python3 qiskit_aqua_example.py
$ python3 qiskit_ignis_example.py
```

### Alternatively, create Qiskit Notebook [here](https://quantum-computing.ibm.com/jupyter)
