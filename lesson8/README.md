# <a href="https://goo.gl/ibFiqR">Lesson 8</a>: Data Analysis

# Install NumPy, SciPy, Matplotlib, and pandas on a Raspberry Pi — replace python-* with python3-* if using Python 3

sudo apt-get update

sudo apt-get install build-essential

sudo apt-get install python-dev python3-dev

sudo apt-get install python-setuptools python3-setuptools

sudo apt-get install python-numpy python3-numpy

sudo apt-get install python-scipy python3-scipy

sudo apt-get install python-matplotlib python3-matplotlib

sudo apt-get install python-pandas python3-pandas

# Install the latest scikit-learn by pip instead of "sudo apt-get install python-sklearn" on a Raspberry Pi

sudo apt-get install libopenblas-dev

sudo pip install -U pip

sudo pip install -U scikit-learn

# Use conda on Windows, or pip on Linux and macOS to install or update Python data analysis packages

sudo pip install -U pip 

sudo pip install -U numpy scipy scikit-learn matplotlib pandas

# Install Apache MXNet for deep learning on macOS

sudo pip install -U mxnet
