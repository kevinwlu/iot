# <a href="https://goo.gl/ibFiqR">Lesson 8</a>: Data Analysis

# Install (or update) Python data analysis packages on a Raspberry Pi
pi@iotu:~ $ sudo apt-get update
pi@iotu:~ $ sudo apt-get dist-upgrade
pi@iotu:~ $ sudo apt-get install build-essential
pi@iotu:~ $ sudo apt-get install python-dev python3-dev
pi@iotu:~ $ sudo apt-get install python-setuptools python3-setuptools
pi@iotu:~ $ sudo apt-get install python-numpy python3-numpy
pi@iotu:~ $ sudo apt-get install python-scipy python3-scipy
pi@iotu:~ $ sudo apt-get install python-matplotlib python3-matplotlib
pi@iotu:~ $ sudo apt-get install python-pandas python3-pandas

# Install the latest scikit-learn by pip instead of "sudo apt-get install python-sklearn"
pi@iotu:~ $ sudo apt-get install libatlas-dev libatlas3gf-base
pi@iotu:~ $ sudo update-alternatives --set libblas.so.3 \
> /usr/lib/atlas-base/atlas/libblas.so.3
pi@iotu:~ $ sudo update-alternatives --set liblapack.so.3 \
> /usr/lib/atlas-base/atlas/liblapack.so.3
pi@iotu:~ $ sudo pip install -U pip
pi@iotu:~ $ sudo pip install -U scikit-learn
pi@iotu:~ $ 
