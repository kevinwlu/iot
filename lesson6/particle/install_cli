# Shortcut URL: https://particle.io/install-cli
# Source URL: https://raw.githubusercontent.com/spark/particle-cli-wrapper/master/installer/unix/install-cli

#!/bin/bash
# Install the Particle Command Line Interface (CLI)
#
# This installs a binary wrapper to the home directory.
#
# That binary wrapper will download its own version of Node to ~/.particle
#
# It will also download the particle-cli npm module which contains the
# actual Particle CLI logic to ~/.particle/node_modules.
# When a new version of the particle-cli is released, the binary wrapper
# will update to the latest version in the background.
#
# Run CHANNEL=beta ./install-cli to use the beta version

CHANNEL=${CHANNEL:-master}
BINARY="particle"
DEST_PATH="$HOME/bin"
DEST="$DEST_PATH/$BINARY"
MANIFEST_URL="https://binaries.particle.io/cli/${CHANNEL}/manifest.json"
SHELL_CONFIG="$HOME/.bash_profile"

# setup for zsh if that's the prefered shell
if [ -n "$($SHELL -c 'echo $ZSH_VERSION')" ]; then
   SHELL_CONFIG="$HOME/.zprofile"
fi

# Compute OS and architecture
UNAME=$(uname -s)
case $UNAME in
    Linux)
        OS="linux"
        ;;
    Darwin)
        OS="darwin"
        ;;
    *)
        echo "Don't know how to install the Particle CLI on $UNAME"
        exit 1
        ;;
esac

PROCESSOR=$(uname -m)
case $PROCESSOR in
    x86_64)
        ARCH="amd64"
        ;;
    i686)
        ARCH="386"
        ;;
    arm*)
        ARCH="arm"
        ;;
    *)
        echo "Don't know how to install the Particle CLI for $PROCESSOR"
        exit 1
        ;;
esac

# Download JSON manifest with latest CLI binary
echo "Installing the Particle CLI to $DEST"

BINARY_URL=$(curl -s $MANIFEST_URL | python -c "import sys, json; print(json.load(sys.stdin)['builds']['$OS']['$ARCH']['url'])")

# Download binary
mkdir -p "$DEST_PATH"

if [ -z "$LOCAL_BINARY" ]; then
    curl -s "$BINARY_URL.gz" | gunzip > "$DEST"
else
    cp "$LOCAL_BINARY" "$DEST"
fi

chmod +x "$DEST"

# Install dependencies
function program_exists {
    hash "$1" 2> /dev/null
}

function install_program {
    prog="$1"

    if ! program_exists "$prog"; then
        if [ "$OS" = "linux" ]; then
            if program_exists "apt-get"; then
                echo "Installing dependency $prog"
                sudo apt-get install -y "$prog"
                return
            fi
        else
            if program_exists "brew"; then
                echo "Installing dependency $prog"
                brew install "$prog"
                return
            fi
        fi
        echo "The Particle CLI uses $prog. Install it for your OS"
    fi
}

install_program "dfu-util"
install_program "openssl"

# Run binary for the first time to make it install Node and the
# particle-cli npm module
"$DEST"

# Add ~/bin to the path
function file_contains {
    grep "$2" "$1" 1>/dev/null 2>&1
}

if ! file_contains "$SHELL_CONFIG" "\$HOME/bin"; then
    cat >> "$SHELL_CONFIG" <<EOL

# set PATH so it includes user's private bin if it exists
if [ -d "\$HOME/bin" ] ; then
    PATH="\$HOME/bin:\$PATH"
fi
EOL
fi

echo "Get started by running \"$BINARY login\""
echo "If that doesn't work, open a new terminal and make sure $DEST_PATH is in your shell path."
echo "If you previously installed the CLI with npm, run \"npm uninstall -g particle-cli\""
