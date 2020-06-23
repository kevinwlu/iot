# Lesson 8: Data Analysis
* [ATLAS](https://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software) (Automatically Tuned Linear Algebra Software)
* [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) (Basic Linear Algebra Subprograms)
* [NumPy](https://en.wikipedia.org/wiki/NumPy)
* [SciPy](https://en.wikipedia.org/wiki/SciPy)
* [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
* [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
* [Pandas](https://en.wikipedia.org/wiki/Pandas_(software))
* [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow)
* [Keras](https://en.wikipedia.org/wiki/Keras)

## Lab 8A: Examples

### On Windows, open Git Bash and install Python packages as follows
```sh
$ python -m pip install -U numpy scipy scikit-learn matplotlib pandas tensorflow keras
```
* If could not find a version that satisfies the requirement tensorflow (from versons: none) or no matching distribution found for tensorflow, turn on Developer Mode, join Windows Insider Program, upgrade Windows, install [Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/install/), download a [TensorFlow Docker image](https://www.tensorflow.org/install/docker), open Windows PowerShell, and run the following commands
```sh
$ docker pull tensorflow/tensorflow
$ docker run -it tensorflow/tensorflow bash
# apt update
# apt full-upgrade
# apt install git-all
# git clone https://github.com/kevinwlu/iot.git
# pip install keras
# cd iot/lesson8
# python keras_diabetes.py
# python keras_first_network.py
# exit
```
### On macOS/Linux, open a terminal and install Python packages as follows
```sh
$ sudo pip3 install -U numpy scipy scikit-learn matplotlib pandas tensorflow keras
```
### On Raspberry Pi, open a terminal and install Python packages as follows
```sh
$ sudo apt update
$ sudo apt install python3-scipy
$ sudo apt install python3-matplotlib
$ sudo apt install python3-pandas
$ sudo apt install libopenblas-dev
$ sudo apt install libatlas-base-dev
$ sudo pip3 install -U numpy
$ sudo pip3 install --only-binary :all: -U scikit-learn
$ sudo pip3 install -U tensorflow
$ sudo pip3 install -U keras==2.3.1
```
### Enable [X11](https://en.wikipedia.org/wiki/X_Window_System) forwarding with [SSH -Y](http://man.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh.1#Y) on a PC to run code on Raspberry Pi without VNC Viewer

#### For Windows, download and install [Xming](https://sourceforge.net/projects/xming/), and open Git Bash
```sh
$ export DISPLAY=localhost:0
$ ssh -Y pi@xxx.xxx.xxx.xxx
```
#### For macOS, download and install [XQuartz](https://www.xquartz.org/), and open a terminal
```sh
$ ssh -Y pi@xxx.xxx.xxx.xxx
```
#### For Linux (most distributions have the X server installed), open a terminal
```sh
$ ssh -Y pi@xxx.xxx.xxx.xxx
```
### Run Python code
```sh
$ cd ~/iot/lesson8
$ python3 pyplot_simple.py
$ python3 simple_plot.py
$ python3 pyplot_formatstr.py
$ python3 ticklabels_demo_rotation.py
$ python3 pyplot_three.py
$ python3 pyplot_two_subplots.py
$ python3 pyplot_scales.py
$ python3 pyplot_annotate.py
$ python3 major_minor_demo1.py
$ python3 legend_demo.py
```
## Lab 8B: Data Analysis

### Histograms, box plots, regression, and classification
```sh
$ python3 scatter_demo.py
$ python3 histogram_demo_features.py
$ python3 pyplot_text.py
$ python3 histogram_demo_extended.py
$ python3 boxplot_demo.py
$ python3 linreg.py
$ python3 interpolation.py
$ python3 plot_lda.py
$ python3 plot_lda_qda.py
$ python3 plt_final.py
```

### Cross-validation
```sh
$ python3 plt_cv2.py
$ python3 plot_cv_predict.py
$ python3 plot_cv_diabetes.py
```

### Keras and TensorFlow

[Deep learning project in Python with Keras](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/)
```sh
$ python3 keras_diabetes.py
$ python3 keras_first_network.py
```

### Titanic example
```sh
$ cp train.csv ~/demo
$ cp test.csv ~/demo
$ cp titanic_1.py ~/demo
$ cp titanic_2.py ~/demo
$ cd ~/demo
$ python3 titanic_1.py
$ python3 titanic_2.py
```
