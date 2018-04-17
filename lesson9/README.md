# <a href="https://goo.gl/RIzzfl">Lesson 9</a>: NETCONF and YANG

# Install and run pyang on a Raspberry Pi

sudo pip3 install -U pyang

cp ~/iot/lesson9/intrusiondetection.yang ~/demo

cd demo

pyang -f yin -o intrusiondetection.yin intrusiondetection.yang

pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef

# Install the Python 2 PlantUML module on a laptop or Raspberry Pi

sudo pip install -U plantuml

# Run PlantUML to create a sequence diagram in PNG

python -m plantuml intrusiondetection.uml

# Install and run GIMP to display a PNG file (Run SSH -Y to enable X11 forwarding as an alternative to VNC Viewer)

sudo apt-get update

sudo apt-get install gimp

gimp -a intrusiondetection.png

# Install Libnetconf and Libssh on Ubuntu (build instructions on slides)

git clone https://github.com/CESNET/libnetconf.git

sudo apt-get install libtool libtool-bin

sudo apt-get install libxml2-dev libxslt1-dev

sudo apt-get install libcurl4-openssl-dev xsltproc

sudo apt-get install python-setuptools cmake

sudo apt-get install zlib1g-dev libssl-dev

sudo pip install pyang

git clone https://git.libssh.org/projects/libssh.git

# Install and run Netopeer on Ubuntu (build instructions on slides)

git clone https://github.com/CESNET/netopeer.git

sudo apt-get install python-libxml2

sudo /usr/local/bin/netopeer-server -d

sudo apt-get install libreadline-dev

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

cp ~/lesson9/Dockerfile ~/demo

cd ~/demo

docker build -t curl_docker .

docker run curl_docker

docker images

# Build the tiniest blockchain (by Gerald Nash)

cd ~/iot/lesson9

python3 snakecoin.py
