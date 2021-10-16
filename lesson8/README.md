# Lesson 8: Data Analysis
* [Data analysis](https://en.wikipedia.org/wiki/Data_analysis)
  * [Big data](https://en.wikipedia.org/wiki/Big_data)
  * [Data science](https://en.wikipedia.org/wiki/Data_science)
  * [Kaggle](https://www.kaggle.com/)
  * [Google Dataset Search](https://datasetsearch.research.google.com/)
  * [Google Books Ngram Viewer](https://books.google.com/ngrams)
  * [IEEE DataPort](https://ieee-dataport.org/)
  * [Datasets](https://github.com/kevinwlu/iot/tree/master/lesson8/datasets)
* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) (AI)
  * [One Hundread Year Study on Artificial Intelligence](https://ai100.stanford.edu/)
  * [Association for the Advancement of Artificial Intelligence](https://en.wikipedia.org/wiki/Association_for_the_Advancement_of_Artificial_Intelligence) (AAAI)
  * [Partnership on AI](https://en.wikipedia.org/wiki/Partnership_on_AI)
  * [Explainable AI](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence)
  * [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)
  * [Google AI](https://en.wikipedia.org/wiki/Google_AI)
  * [AI Hub](https://aihub.cloud.google.com/u/0/)
  * [Colab](https://colab.research.google.com/notebooks/welcome.ipynb)
* [NumPy](https://en.wikipedia.org/wiki/NumPy)
  * [Linear algebra](https://en.wikipedia.org/wiki/Linear_algebra)
  * [Automatically Tuned Linear Algebra Software](https://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software) (ATLAS)
  * [Basic Linear Algebra Subprograms](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) (BLAS)
  * [Quickstart](https://numpy.org/devdocs/user/quickstart.html)
* [SciPy](https://en.wikipedia.org/wiki/SciPy)
  * [Linear regression](https://en.wikipedia.org/wiki/Linear_regression)
  * [Lasso](https://en.wikipedia.org/wiki/Lasso_(statistics))
  * [Interpolation](https://en.wikipedia.org/wiki/Interpolation)
  * [Overfitting](https://en.wikipedia.org/wiki/Overfitting)
* [Scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn)
  * [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification)
  * [Cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics))
  * [Support-vector machine](https://en.wikipedia.org/wiki/Support-vector_machine) (SVM)
  * [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)
  * [F-score](https://en.wikipedia.org/wiki/F-score)
* [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
  * [Data visualization ](https://en.wikipedia.org/wiki/Data_visualization)
  * [Histogram](https://en.wikipedia.org/wiki/Histogram)
  * [Box plot](https://en.wikipedia.org/wiki/Box_plot)
* [Pandas](https://en.wikipedia.org/wiki/Pandas_(software))
* [Machine learning](https://en.wikipedia.org/wiki/Machine_learning) (ML)
  * [List of datasets for machine learning research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research)
  * [Federated learning](https://en.wikipedia.org/wiki/Federated_learning)
  * [tinyML Foundaton](https://www.tinyml.org/)
  * [Harvard Fundamentals of TinyML Course](https://online-learning.harvard.edu/course/fundamentals-tinyml) 
  * [Harvard CS249r: Tiny Machine Learning](https://sites.google.com/g.harvard.edu/tinyml/home)
  * [Edge Impulse](https://www.edgeimpulse.com/)
  * [Edge Impulse and TinyML on Raspberry Pi](https://www.raspberrypi.com/news/edge-impulse-and-tinyml-on-raspberry-pi/)
  * [Infxl](https://infxl.com/)
* [Deep learning](https://en.wikipedia.org/wiki/Deep_learning) (DL)
  * [Comparison of deep-learning software](https://en.wikipedia.org/wiki/Comparison_of_deep-learning_software)
  * [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow)
  * [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers)
  * [Keras](https://en.wikipedia.org/wiki/Keras)
  * [OpenAI](https://en.wikipedia.org/wiki/OpenAI)
  * [OpenAI Codex](https://openai.com/blog/openai-codex/)
  * [GPT-3](https://en.wikipedia.org/wiki/GPT-3)
  * [MindSpore](https://github.com/mindspore-ai/mindspore) deep learning training/inference framework
* [Movidius Neural Compute Stick](https://github.com/movidius/ncsdk.git) (NCS)
  * [Intel NCS2](https://software.intel.com/content/www/us/en/develop/hardware/neural-compute-stick.html)
  * [Intel OpenVINO](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html) (Visual Inference and Neural network Optimization)
## Lab 8A: Examples

### On Windows with [WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10), run PowerShell as Administrator Windows and install Python packages as follows
```sh
$ pip install -U numpy scipy scikit-learn matplotlib pandas tensorflow keras
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
### Enable [X11](https://en.wikipedia.org/wiki/X_Window_System) forwarding with [SSH -Y](http://man.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/ssh.1#Y) on a computer to run code on Raspberry Pi without VNC Viewer

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
### Numpy array
```sh
$ python3
>>> import numpy as np
>>> a = np.arange(6)
>>> a
>>> b = np.arange(12).reshape(4, 3)
>>> b
>>> c = np.arange(24).reshape(2, 3, 4)
>>> c
>>> b.shape
>>> b.reshape(-1)
>>> b.reshape(-1, 1)
>>> b.reshape(2, -1)
>>> d = np.array([20, 30, 40, 50])
>>> e = np.arange(4)
>>> f = d-e
>>> f
>>> e**2
>>> A = np.array([[1, 1], [0, 1]])
>>> B = np.array([[2, 0], [3, 4]])
>>> A*B
>>> A.dot(B)
>>> np.dot(A, B)
>>> g = np.ones((2, 3), dtype=int)
>>> g
>>> h = np.random.random((2, 3))
>>> h
>>> g *= 3
>>> g
>>> h += g
>>> h
>>> k = np.random.random((2, 3))
>>> k
>>> k.sum()
>>> k.min()
>>> k.max()
>>> m = np.arange(12).reshape(3, 4)
>>> m
>>> m.sum(axis = 0)
>>> m.min(axis = 1)
>>> m.cumsum(axis = 1)
>>> n = np.arange(5)
>>> n
>>> n[[1, 3, 4]] = 0
>>> n
>>> exit()
```
### Review and Run Python code
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

### Histograms, box plots, regression, and interpolation
```sh
$ python3 scatter_demo.py
$ python3 histogram_demo_features.py
$ python3 pyplot_text.py
$ python3 histogram_demo_extended.py
$ python3 boxplot_demo.py
$ python3 linreg.py
$ python3 interpolation.py
```

### Classification, cross-validation (CV), and support-vector machine (SVM)
```sh
$ python3 plot_lda.py
$ python3 plot_lda_qda.py
$ python3 plot_cv_predict.py
$ python3 plot_cv_diabetes.py
$ python3 traffic.py
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

## Lab 8B: Data Analysis

### Analyze Raspberry Pi date/time and CPU usage/temperature of Lab 7B

* [Insert four charts](https://support.google.com/docs/answer/63824) including time series, two histograms, and a scatter plot with a linear trendline
* Save the Google sheet in CSV format to ~/demo
* Copy ~/iot/lesson8/plt_final.py and plt_cv2.py to ~/demo
* Edit them to read the CSV file
* Show seven figures including time series, two histograms, two box plots, a scatter plot with a linear regression line, and cross-validation prediction with temperature as target
* Include required title/labels, and add legend or adjust ticks as needed
```sh
$ cd ~/demo
$ cp ~/iot/lesson8/plt_final.py .
$ cp ~/iot/lesson8/plt_cv2.py .
$ nano plt_final.py
```
> data = read_csv('rpidata.csv')
```sh
$ nano plt_cv2.py
```
> X = read_csv('rpidata.csv', usecols=[1])

> y = read_csv('rpidata.csv', usecols=[2])
```sh
$ python3 plt_final.py
$ python3 plt_cv2.py
```
