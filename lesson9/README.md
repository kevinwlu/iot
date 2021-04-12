# Lesson 9: NETCONF and YANG
* [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
* [YANG](https://en.wikipedia.org/wiki/YANG)
* [Namespace](https://en.wikipedia.org/wiki/Namespace)
* [Remote procedure call](https://en.wikipedia.org/wiki/Remote_procedure_call) (RPC)
* [Extensible Markup Language](https://en.wikipedia.org/wiki/XML) (XML)
* [Extensible Stylesheet Language Transformations](https://en.wikipedia.org/wiki/XSLT) (XSLT)
* [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (UML)
* [PlantUML](https://en.wikipedia.org/wiki/PlantUML)
* [Portable Network Graphics](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (PNG)
* [GNU Image Manipulation Program](https://en.wikipedia.org/wiki/GIMP) (GIMP)
* [Pinta](https://en.wikipedia.org/wiki/Pinta_(software))
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
$
```

## Lab 9B: Qiskit

### [IBM Quantum Computing](https://www.ibm.com/quantum-computing/)

### Create an IBM Quantum Experience [account](https://quantum-computing.ibm.com/)
* [User Guides](https://quantum-computing.ibm.com/docs/)
* [Access systems with your account](https://quantum-computing.ibm.com/docs/manage/account/ibmq)

### IBM Quantum Lab Qiskit Tutorials include a core reference set of [notebooks](https://quantum-computing.ibm.com/jupyter) outlining the features of Qiskit

### Learn quantum computation using Qiskit: [textbook](https://qiskit.org/textbook/preface.html)

### [Start Qiskit on the cloud](https://qiskit.org/documentation/getting_started.html)

### Start Qiskit locally on Windows, macOS, or Raspberry Pi

#### Open Git Bash on Windows, install Qiskit, copy and save API token from the [account](https://quantum-computing.ibm.com/account), and run examples
```sh
$ pip install qiskit qiskit[visualization]
$ python -i
>>> from qiskit import IBMQ
>>> IBMQ.save_account('MY_API_TOKEN')
>>> exit()
$ cd ~/iot/lesson9
$ python qiskit_terra_example.py
$ python qiskit_aer_example.py
$ python qiskit_aqua_example.py
$ python qiskit_ignis_example.py
```
#### On macOS, install Qiskit and copy and save API token from the [account](https://quantum-computing.ibm.com/account), and run examples
```sh
$ sudo pip3 install qiskit qiskit[visualization]
$ python3
>>> from qiskit import IBMQ
>>> IBMQ.save_account('MY_API_TOKEN')
>>> exit()
$ cd ~/iot/lesson9
$ python3 qiskit_terra_example.py
$ python3 qiskit_aer_example.py
$ python3 qiskit_aqua_example.py
$ python3 qiskit_ignis_example.py
```

#### SSH -Y to Raspberry Pi, follow [RasQberry](https://medium.com/qiskit/rasqberry-quantum-computing-is-the-coolest-project-for-raspberry-pi-3f64bec5a133) to install Qiskit, copy and save API token from the [account](https://quantum-computing.ibm.com/account), and run examples
```sh
$ sudo sed -i 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=1024/' /etc/dphys-swapfile
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo /etc/init.d/dphys-swapfile start
$ pip3 install setuptools-rust
$ curl -o get_rustup.sh -s https://sh.rustup.rs
$ sh ./get_rustup.sh -y
$ source ~/.cargo/env
$ pip3 install --prefer-binary retworkx
$ sudo apt -y install cmake libatlas-base-dev git
$ git clone https://github.com/sunqm/libcint.git
$ mkdir -p libcint/build && cd libcint/build
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr/local/ ..
$ sudo make install
$ cd
$ pip3 install --prefer-binary pyscf cython
$ pip3 install --prefer-binary qiskit-terra
$ pip3 install --prefer-binary qiskit-ignis
$ pip3 install --prefer-binary qiskit-ibmq-provider
$ pip3 install --prefer-binary qiskit-aqua
$ pip3 install --prefer-binary qiskit-aer
$ pip3 install --prefer-binary qiskit[visualization]
$ python3
>>> from qiskit import IBMQ
>>> IBMQ.save_account('MY_API_TOKEN')
>>> IBMQ.load_account()
<AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>
>>> IBMQ.providers()
[<AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>]
>>> provider = IBMQ.get_provider(hub='ibm-q')
>>> provider.backends()
[<IBMQSimulator('ibmq_qasm_simulator') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmqx2') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_16_melbourne') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_armonk') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_athens') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_santiago') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_lima') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_belem') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_quito') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_statevector') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_mps') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_extended_stabilizer') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_stabilizer') from IBMQ(hub='ibm-q', group='open', project='main')>]
>>> backend = provider.get_backend('ibmq_lima')
>>> backend
<IBMQBackend('ibmq_lima') from IBMQ(hub='ibm-q', group='open', project='main')>
>>> exit()
$ cd ~/iot/lesson9
$ python3 qiskit_terra_example.py
$ python3 qiskit_aer_example.py
$ python3 qiskit_aqua_example.py
$ python3 qiskit_ignis_example.py
```
