# Shortcut: https://particle.io/install-pi
# Source URL: https://raw.githubusercontent.com/spark/particle-agent/master/bin/cloud-install

#!/bin/bash

PACKAGES_DIR=/tmp/particle-agent-packages-$BASHPID
AGENT_VER=${AGENT_VER:-0.2.4-1}
UNICODE_DISPLAY_WIDTH_VER=${UNICODE_DISPLAY_WIDTH_VER:-1.1.1-1}
WHIRLY_VER=${WHIRLY_VER:-0.2.3-1}
PARTICLERB_VER=${PARTICLERB_VER:-1.3.1-1}

echo -e "Installing the Particle Agent\n"

echo -e "Downloading packages\n"

curl -# -L --create-dirs \
  https://github.com/spark/particle-agent/releases/download/v${AGENT_VER}/particle-agent_${AGENT_VER}_all.deb -o $PACKAGES_DIR/particle-agent_${AGENT_VER}_all.deb \
  https://github.com/spark/ruby-unicode-display-width/releases/download/debian%2F${UNICODE_DISPLAY_WIDTH_VER}/ruby-unicode-display-width_${UNICODE_DISPLAY_WIDTH_VER}_all.deb -o $PACKAGES_DIR/ruby-unicode-display-width_${UNICODE_DISPLAY_WIDTH_VER}_all.deb \
  https://github.com/spark/ruby-whirly/releases/download/debian%2F${WHIRLY_VER}/ruby-whirly_${WHIRLY_VER}_all.deb -o $PACKAGES_DIR/ruby-whirly_${WHIRLY_VER}_all.deb \
  https://github.com/spark/ruby-particlerb/releases/download/debian%2F${PARTICLERB_VER}/ruby-particlerb_${PARTICLERB_VER}_all.deb -o $PACKAGES_DIR/ruby-particlerb_${PARTICLERB_VER}_all.deb

echo -e "\nInstalling packages\n"
sudo apt-get install -y libssl-dev
sudo dpkg --install \
  $PACKAGES_DIR/particle-agent_${AGENT_VER}_all.deb \
  $PACKAGES_DIR/ruby-unicode-display-width_${UNICODE_DISPLAY_WIDTH_VER}_all.deb \
  $PACKAGES_DIR/ruby-whirly_${WHIRLY_VER}_all.deb \
  $PACKAGES_DIR/ruby-particlerb_${PARTICLERB_VER}_all.deb
sudo apt-get install -f -y

# Flush stdin
read -N 10000000 -t 0.01

echo -e "\nRunning sudo particle-agent setup\n"

sudo particle-agent setup
