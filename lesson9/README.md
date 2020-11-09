# Lesson 9: NETCONF and YANG
* [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
* [YANG](https://en.wikipedia.org/wiki/YANG)
* [Namespace](https://en.wikipedia.org/wiki/Namespace)
* [Remote procedure call](https://en.wikipedia.org/wiki/Remote_procedure_call) (RPC)
* [Extensible Markup Language](https://en.wikipedia.org/wiki/XML) (XML)
* [Extensible Stylesheet Language Transformations](https://en.wikipedia.org/wiki/XSLT) (XSLT)
* [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (UML)
* [PlantUML](https://en.wikipedia.org/wiki/PlantUML)
* [GNU Image Manipulation Program](https://en.wikipedia.org/wiki/GIMP) (GIMP)
* [Pinta](https://en.wikipedia.org/wiki/Pinta_(software))
* [Portable Network Graphics](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (PNG)
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
$ cat intrusiondetection.yang
$ pyang -f yin -o intrusiondetection.yin intrusiondetection.yang
$ cat intrusiondetection.yin
$ pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef
$ cat intrusiondetection.uml
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
^C
$
```

## Lab 9B: Qiskit

### Learn quantum computation using Qiskit [textbook](https://qiskit.org/textbook/preface.html)

### Create an IBM Quantum Experience [account](https://quantum-computing.ibm.com/)

### IBM Quantum Lab [Qiskit Tutorials](https://quantum-computing.ibm.com/jupyter) include a core reference set of notebooks outlining the features of Qiskit

### Alternatively, install qiskit on a laptop (not Raspberry Pi)

### Copy API token from [account](https://quantum-computing.ibm.com/account), and save API token

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
