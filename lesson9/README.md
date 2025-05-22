# Lesson 9: YANG

* [Mobile device management](https://en.wikipedia.org/wiki/Mobile_device_management)
  * [1NCE](https://1nce.com/)
  * [AVSystem](https://www.avsystem.com/)
  * [EdgeIQ](http://www.edgeiq.ai/)
  * [IoTerop](https://ioterop.com/)
  * [Pelion](https://pelion.com/)
* [Simple Network Management Protocol](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) (SNMP)
  * [Management information base](https://en.wikipedia.org/wiki/Management_information_base) (MIB)
  * [Object identifier](https://en.wikipedia.org/wiki/Object_identifier) (OID)
* [Information Technology Infrastructure Library](https://en.wikipedia.org/wiki/ITIL) (ITIL)
* [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
  * [IETF RFC 6241](https://datatracker.ietf.org/doc/html/rfc6241)
* [YANG](https://en.wikipedia.org/wiki/YANG) ([Yet Another](https://en.wikipedia.org/wiki/Yet_another) Next Generation)
  * [IETF RFC 7950](https://datatracker.ietf.org/doc/html/rfc7950)
  * [Namespace](https://en.wikipedia.org/wiki/Namespace)
  * [Remote procedure call](https://en.wikipedia.org/wiki/Remote_procedure_call) (RPC)
  * [Extensible Markup Language](https://en.wikipedia.org/wiki/XML) (XML)
    * [Automatic Test Markup Language](https://en.wikipedia.org/wiki/ATML) (ATML)
  * [Extensible Stylesheet Language Transformations](https://en.wikipedia.org/wiki/XSLT) (XSLT)
  * [pyang](https://github.com/mbj4668/pyang)
* [Tail-f Systems](https://www.tail-f.com/), a [Cisco](https://en.wikipedia.org/wiki/Cisco) company
* [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (UML)
  * [List of Unified Modeling Language tools](https://en.wikipedia.org/wiki/List_of_Unified_Modeling_Language_tools)
  * [UMLet](https://en.wikipedia.org/wiki/UMLet)
  * [List of concept- and mind-mapping software](https://en.wikipedia.org/wiki/List_of_concept-_and_mind-mapping_software)
  * [PlantUML](https://en.wikipedia.org/wiki/PlantUML)
  * [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) (Portable Network Graphics)
  * [GIMP](https://en.wikipedia.org/wiki/GIMP) (GNU Image Manipulation Program)
  * [Pinta](https://en.wikipedia.org/wiki/Pinta_(software))
* [NetHogs](https://github.com/raboof/nethogs)
* [OpenNMS](https://en.wikipedia.org/wiki/OpenNMS)
* [Prometheus](https://en.wikipedia.org/wiki/Prometheus_(software))
* [Splunk](https://en.wikipedia.org/wiki/Splunk)
* [Infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC)
* [Comparison of open-source configuration management software](https://en.wikipedia.org/wiki/Comparison_of_open-source_configuration_management_software)
  * [Ansible](https://en.wikipedia.org/wiki/Ansible_(software))
  * [CFEngine](https://en.wikipedia.org/wiki/CFEngine)
  * [Progress Chef](https://en.wikipedia.org/wiki/Progress_Chef)
  * [Puppet](https://en.wikipedia.org/wiki/Puppet_(software))
  * [Terraform](https://en.wikipedia.org/wiki/Terraform_(software))
* [Chaos engineering](https://en.wikipedia.org/wiki/Chaos_engineering)
* [Cloud Native Computing Foundation](https://en.wikipedia.org/wiki/Cloud_Native_Computing_Foundation) (CNCF)
* [Serverless computing](https://en.wikipedia.org/wiki/Serverless_computing)
* [Orchestration (computing)](https://en.wikipedia.org/wiki/Orchestration_(computing))
* [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) (K8s)
  * Other [numeronym](https://en.wikipedia.org/wiki/Numeronym) such as i18n and l10n ([internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization))
  * [Learn Linux TV](https://www.youtube.com/@LearnLinuxTV) | [How to build your own Raspberry Pi Kubernetes Cluster](https://www.youtube.com/watch?v=B2wAJ5FLOYw)
* [Apache Mesos](https://en.wikipedia.org/wiki/Apache_Mesos)
* [OpenShift](https://en.wikipedia.org/wiki/OpenShift)
* [Microservices](https://en.wikipedia.org/wiki/Microservices)
  * [Monolithic application](https://en.wikipedia.org/wiki/Monolithic_application)
* [Creatio](https://en.wikipedia.org/wiki/Creatio) process automation

## Lab 9: YANG
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

