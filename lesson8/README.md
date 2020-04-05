# <a href="https://goo.gl/ibFiqR">Lesson 8</a>: Data Analysis

## Lab A: Examples

### Install SciPy, Matplotlib, pandas, and dependencies on Raspberry Pi
```sh
$ sudo apt update
$ sudo apt install python3-scipy
$ sudo apt install python3-matplotlib
$ sudo apt install python3-pandas
$ sudo apt install libopenblas-dev
$ sudo apt install libatlas-base-dev
```
### Install NumPy, scikit-learn, TensorFlow, and Keras on Raspberry Pi
```sh
$ sudo pip3 install -U numpy
$ sudo pip3 install --only-binary :all: -U scikit-learn
$ sudo pip3 install -U tensorflow
$ sudo pip3 install -U keras
```
### Enable X11 forwarding with SSH -Y on a PC to run code on Raspberry Pi without VNC Viewer

#### For Windows, follow the instructions, install and configure Xming, and always open Xming before running PuTTY with SSH and X11 forwarding

http://laptops.eng.uci.edu/software-installation/using-linux/how-to-configure-xming-putty

https://sourceforge.net/projects/xming/

https://www.putty.org/

#### For macOS, download and install XQuartz, and enter "ssh -Y" in a terminal

https://www.xquartz.org/

http://man.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh.1#Y

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

## Lab B: Data Analysis

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

https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

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
