# <a href="https://goo.gl/RIzzfl">Lesson 9</a>: NETCONF and YANG

## Install and run pyang on a Raspberry Pi

sudo apt-get install libxml2-dev libxslt1-dev

sudo pip3 install -U lxml pyang

cp ~/iot/lesson9/intrusiondetection.yang ~/demo

cd demo

pyang -f yin -o intrusiondetection.yin intrusiondetection.yang

pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef

## Install the Python 2 PlantUML module on a laptop or Raspberry Pi

sudo pip3 install -U plantuml

## Run PlantUML to create a sequence diagram in PNG

python3 -m plantuml intrusiondetection.uml

## Install and run GIMP and Pinta to display a PNG file (Enable X11 forwarding by SSH -Y on macOS or run Xming then PuTTY with X11 forwarding on Windows 10 as an alternative to VNC Viewer)

cd

sudo apt-get update

sudo apt-get install gimp pinta

cd demo

pinta intrusiondetection.png

gimp -h

gimp -a intrusiondetection.png
