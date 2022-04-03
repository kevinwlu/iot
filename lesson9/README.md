# Lesson 9: YANG and Qiskit
* [SNMP](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) (Simple Network Management Protocol)
* [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
  * [IETF RFC 6241](https://datatracker.ietf.org/doc/html/rfc6241)
* [YANG](https://en.wikipedia.org/wiki/YANG) ([Yet Another](https://en.wikipedia.org/wiki/Yet_another) Next Generation)
  * [IETF RFC 7950](https://datatracker.ietf.org/doc/html/rfc7950)
  * [Namespace](https://en.wikipedia.org/wiki/Namespace)
  * [Remote procedure call](https://en.wikipedia.org/wiki/Remote_procedure_call) (RPC)
  * [Extensible Markup Language](https://en.wikipedia.org/wiki/XML) (XML)
  * [Extensible Stylesheet Language Transformations](https://en.wikipedia.org/wiki/XSLT) (XSLT)
  * [pyang](https://github.com/mbj4668/pyang)
* [PlantUML](https://en.wikipedia.org/wiki/PlantUML)
  * [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (UML)
  * [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (Portable Network Graphics)
  * [GIMP](https://en.wikipedia.org/wiki/GIMP) (GNU Image Manipulation Program)
  * [Pinta](https://en.wikipedia.org/wiki/Pinta_(software))
* [Chaos engineering](https://en.wikipedia.org/wiki/Chaos_engineering)
* [Cloud Native Computing Foundation](https://en.wikipedia.org/wiki/Cloud_Native_Computing_Foundation) (CNCF)
* [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) (K8s)
  * Other [numeronym](https://en.wikipedia.org/wiki/Numeronym) such as i18n and l10n ([internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization))
  * [Raspberry Pi Kubernetes Cluster](https://wiki.learnlinux.tv/index.php/How_to_build_your_own_Raspberry_Pi_Kubernetes_Cluster)
* [Microservices](https://en.wikipedia.org/wiki/Microservices)
  * [Monolithic application](https://en.wikipedia.org/wiki/Monolithic_application)
* [Creatio](https://en.wikipedia.org/wiki/Creatio) process automation
* [Quantum cryptography](https://en.wikipedia.org/wiki/Quantum_cryptography)
  * [Quantum key distribution](https://en.wikipedia.org/wiki/Quantum_key_distribution)
* [Quantum computing](https://en.wikipedia.org/wiki/Quantum_computing)
  * [Qubit](https://en.wikipedia.org/wiki/Qubit)
  * [Qutrit](https://en.wikipedia.org/wiki/Qutrit)
  * [NQI](https://en.wikipedia.org/wiki/National_Quantum_Initiative_Act) (The National Quantum Initiative Act)
  * [QED-C](https://quantumconsortium.org/) (The Quantum Economic Development Consortium)
  * [Quantum supremacy](https://en.wikipedia.org/wiki/Quantum_supremacy)
  * [Quantum programming](https://en.wikipedia.org/wiki/Quantum_programming)
  * [Quantum volume](https://en.wikipedia.org/wiki/Quantum_volume)
  * [Quantum artificial intelligence](https://en.wikipedia.org/wiki/Quantum_artificial_intelligence)
  * [Quantum optimization algorithms](https://en.wikipedia.org/wiki/Quantum_optimization_algorithms)
  * [List of quantum processors](https://en.wikipedia.org/wiki/List_of_quantum_processors)
  * [Superconducting quantum computing](https://en.wikipedia.org/wiki/Superconducting_quantum_computing)
  * [FLOPS](https://en.wikipedia.org/wiki/FLOPS) (floating point operations per second)
  * [CLOPS](https://research.ibm.com/blog/circuit-layer-operations-per-second) (circuit layer operations per second)
* [IEEE Quantum](https://quantum.ieee.org/)
  * IEEE [P1913](https://standards.ieee.org/ieee/1913/6720/) Software-Defined Quantum Communication
  * IEEE [P2995](https://standards.ieee.org/ieee/2995/10633/) Trial-Use Standard for a Quantum Algorithm Design and Development
  * IEEE [P3120](https://standards.ieee.org/ieee/3120/10751/) Standard for Quantum Computing Architecture
  * IEEE [P3155](https://standards.ieee.org/ieee/3155/10845/) Standard for Programmable Quantum Simulator
  * IEEE [P7130](https://standards.ieee.org/ieee/7130/10680/) Standard for Quantum Technologies Definitions
  * IEEE [P7131](https://standards.ieee.org/ieee/7131/10681/) Standard for Quantum Computing Performance Metrics and Performance Benchmarking
* [Qiskit](https://en.wikipedia.org/wiki/Qiskit)
  * [Qiskit repo](https://github.com/Qiskit)
  * [Fun With Quantum](https://github.com/JanLahmann/Fun-with-Quantum)
  * [RasQberry](https://medium.com/qiskit/rasqberry-quantum-computing-is-the-coolest-project-for-raspberry-pi-3f64bec5a133)
  * [PennyLane](https://github.com/PennyLaneAI/pennylane)
  * [Microsoft Quantum Development Kit Samples](https://github.com/microsoft/Quantum)
  * [Xanadu Strawberry Fields](https://github.com/XanaduAI/strawberryfields)
* [Cryogenics](https://en.wikipedia.org/wiki/Cryogenics)
  * [Bluefors](https://bluefors.com/) [Oy](https://en.wikipedia.org/wiki/Osakeyhti%C3%B6)

## Lab 9A: YANG
* A YANG module can be translated into an alternative XML-based syntax called YIN
* The translated module is called a YIN module
### On Ubuntu or Windows with [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10), open an Ubuntu terminal and install pyang and PlantUML
```sh
$ sudo pip3 install pyang plantuml
$ mkdir ~/demo
$ cp ~/iot/lesson9/intrusiondetection.yang ~/demo
$ cd ~/demo
$ cat intrusiondetection.yang
$ pyang -f yin -o intrusiondetection.yin intrusiondetection.yang
$ cat intrusiondetection.yin
$ pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef
$ cat intrusiondetection.uml
$ python3 -m plantuml intrusiondetection.uml
```

![intrusiondetection.png](/lesson9/intrusiondetection.png)

### On Raspbery Pi
* Install and run pyang
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
* Install PlantUML
```sh
$ sudo pip3 install -U plantuml
```
* Run PlantUML to create a sequence diagram in PNG
```sh
$ python3 -m plantuml intrusiondetection.uml
```
* Install and run GIMP and Pinta to display a PNG file via VNC Viewer
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

### [IBM Quantum Computing](https://www.ibm.com/quantum-computing/)
* [IBM Quantum Roadmap](https://research.ibm.com/blog/ibm-quantum-roadmap)
* [IBM Quantum System One](https://en.wikipedia.org/wiki/IBM_Q_System_One)

### Create an [account](https://quantum-computing.ibm.com/) for the IBM Quantum Composer and the IBM Quantum Lab
* Previously known collectively as the [IBM Quantum Experience](https://en.wikipedia.org/wiki/IBM_Quantum_Experience)
* [User Guides](https://quantum-computing.ibm.com/docs/)
* [Access systems with your account](https://quantum-computing.ibm.com/docs/manage/account/ibmq)
* [Qiskit installation](https://qiskit.org/documentation/getting_started.html): Windows, macOS, and Ubuntu
* [Qiskit tutorials](https://qiskit.org/documentation/tutorials.html)
* IBM Quantum Lab Qiskit Tutorials include a core reference set of [notebooks](https://quantum-computing.ibm.com/jupyter) outlining the features of Qiskit
* Learn quantum computation using Qiskit: [textbook](https://qiskit.org/textbook/preface.html)
* [Qiskit Runtime](https://quantum-computing.ibm.com/lab/docs/iql/runtime/)
  * [Runtime system](https://en.wikipedia.org/wiki/Runtime_system)

### On Windows, macOS, or Ubuntu, install Qiskit, copy and save API token from the [account](https://quantum-computing.ibm.com/account), and run Qiskit examples
* [Qiskit Terra](https://github.com/Qiskit/qiskit-terra)
* [Qiskit Aer](https://github.com/Qiskit/qiskit-aer)
* [Qiskit Aqua](https://github.com/Qiskit/qiskit-aqua) DEPRECATED 2021-04-02
* [Qiskit Ignis](https://github.com/Qiskit/qiskit-ignis)
```sh
$ pip3 install qiskit[visualization]
$ python3
>>> from qiskit import IBMQ
>>> IBMQ.save_account('MY_API_TOKEN')
>>> IBMQ.load_account()
>>> exit()
$ cd ~/iot/lesson9
$ python3 qiskit_terra_example.py
$ python3 qiskit_aer_example.py
$ python3 qiskit_aqua_example.py
$ python3 qiskit_ignis_example.py
```
### SSH -Y to Raspberry Pi, refer to [RasQberry](https://medium.com/qiskit/rasqberry-quantum-computing-is-the-coolest-project-for-raspberry-pi-3f64bec5a133) for installing Qiskit on Raspberry Pi OS, copy and save API token from the [account](https://quantum-computing.ibm.com/account), and run Qiskit examples
* [Qiskit Terra](https://github.com/Qiskit/qiskit-terra)
* [Qiskit Aer](https://github.com/Qiskit/qiskit-aer)
* [Qiskit Aqua](https://github.com/Qiskit/qiskit-aqua) DEPRECATED 2021-04-02
* [Qiskit Ignis](https://github.com/Qiskit/qiskit-ignis)
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
$ sudo pip3 install --prefer-binary pyscf cython
$ sudo pip3 install --prefer-binary 'qiskit[visualization]==0.23.1'
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
<IBMQBackend('ibmq_armonk') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_santiago') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_bogota') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_lima') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_belem') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_quito') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_statevector') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_mps') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_extended_stabilizer') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQSimulator('simulator_stabilizer') from IBMQ(hub='ibm-q', group='open', project='main')>, 
<IBMQBackend('ibmq_manila') from IBMQ(hub='ibm-q', group='open', project='main')>]
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
