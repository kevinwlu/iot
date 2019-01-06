# <a href="https://goo.gl/RIzzfl">Lesson 9</a>: NETCONF and YANG

# Install and run pyang on a Raspberry Pi

sudo pip3 install -U pyang

cp ~/iot/lesson9/intrusiondetection.yang ~/demo

cd demo

pyang -f yin -o intrusiondetection.yin intrusiondetection.yang

pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef

# Install the Python 2 PlantUML module on a laptop or Raspberry Pi

sudo pip3 install -U plantuml

# Run PlantUML to create a sequence diagram in PNG

python3 -m plantuml intrusiondetection.uml

# Install and run GIMP and Pinta to display a PNG file (Run SSH -Y to enable X11 forwarding as an alternative to VNC Viewer)

sudo apt-get update

sudo apt-get install gimp pinta

pinta intrusiondetection.png

gimp -h

gimp -a intrusiondetection.png

# Install Docker on a Raspberry Pi

curl -sSL get.docker.com | sh

# Add pi to the Docker Group as a non-root user (Control-d to logout and reconnect via SSH for this to take effect)

sudo usermod -aG docker pi

# Run Docker images designed to work on ARM under the prefix armhf

docker run -it armhf/alpine /bin/sh

cat /etc/os-release

echo "Hi, this is a tiny Linux distribution!" | base64

echo "SGksIHRoaXMgaXMgYSB0aW55IExpbnV4IGRpc3RyaWJ1dGlvbiEK" | base64 -d

exit

docker run armhf/alpine date

# Build and run new image from Dockerfile

docker images

cp ~/iot/lesson9/Dockerfile ~/demo

cd ~/demo

docker build -t curl_docker .

docker run curl_docker

docker images

# Build the tiniest blockchain (by Gerald Nash)

cd ~/iot/lesson9

python3 hash_value.py

python3 snakecoin.py
