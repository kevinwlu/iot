# <a href="https://goo.gl/RIzzfl">Lesson 9</a>: NETCONF and YANG

# Install and run pyang on a Raspberry Pi

sudo pip install -U pyang

cp ~/iot/lesson9/intrusiondetection.yang ~/demo

cd demo

pyang -f yin -o intrusiondetection.yin intrusiondetection.yang

pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef

# Install the Python PlantUML module on a laptop or Raspberry Pi

sudo pip install -U plantuml

# Run Python PlantUML to create a sequence diagram in PNG

python -m plantuml intrusiondetection.uml

# Install and run GIMP to display a PNG file

$ sudo apt-get update

$ sudo apt-get install gimp

$ gimp -a intrusiondetection.png

# Install Docker on a Raspberry Pi

curl -sSL get.docker.com | sh

# Add pi to the Docker Group

sudo usermod -aG docker pi

# Run Docker images designed to work on ARM under the prefix armhf

docker run -it armhf/alpine /bin/sh

docker run armhf/alpine date

# Build and run new image from Dockerfile

docker build -t curl_docker .

docker run curl_docker
