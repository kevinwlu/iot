# <a href="https://goo.gl/ibFiqR">Lesson 8</a>: Data Analysis

# Install (or update) Python data analysis packages on a Raspberry Pi

sudo apt-get update

sudo apt-get install build-essential

sudo apt-get install python-dev

sudo apt-get install python-setuptools

sudo apt-get install python-numpy

sudo apt-get install python-scipy

sudo apt-get install python-matplotlib

sudo apt-get install python-pandas

# Install the latest scikit-learn by pip instead of "sudo apt-get install python-sklearn"

sudo apt-get install libopenblas-dev

sudo update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libopenblas.so.0

sudo update-alternatives --set liblapack.so.3 /usr/lib/lapack/liblapack.so.3

sudo pip install -U pip

sudo pip install -U scikit-learn

# Use conda on Windows or pip on Linux or macOS to install or update Python data analysis packages

sudo pip install -U pip 

sudo pip install -U numpy scipy scikit-learn matplotlib pandas
