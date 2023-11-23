# Fast Fourier Transform
* [Fast Fourier Transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
  * [Nano33Mic.ino](https://github.com/antigones/nano33micRGB)
  * [XiaoMic.ino](/lesson6/xiao/fft/XiaoMic.ino)
* [arduinoFFT](https://github.com/kosme/arduinoFFT) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library
* [PDM library](https://github.com/arduino/ArduinoCore-nRF528x-mbedos/tree/master/libraries/PDM) is a read-only archived repository
  * Arduino IDE > File > Examples > Examples for Seeed XIAO BLE Sense - nRF52840 > PDM
* [Signal processing](https://en.wikipedia.org/wiki/Signal_processing)  
  * [Autocorrelation](https://en.wikipedia.org/wiki/Autocorrelation)
  * [Sampling](https://en.wikipedia.org/wiki/Sampling_(signal_processing))
  * [Nyquist frequency](https://en.wikipedia.org/wiki/Nyquist_frequency)
* [Online tone generator](https://onlinetonegenerator.com/)
* [Voice frequency](https://en.wikipedia.org/wiki/Voice_frequency)
* [Periodogram](https://en.wikipedia.org/wiki/Periodogram)
* [Spectral density estimation](https://en.wikipedia.org/wiki/Spectral_density_estimation)
* [Autoregressive–moving-average model](https://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model) (ARMA)
```
$ python3
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> from scipy import signal
>>> data=pd.read_csv("data.csv")
>>> plt.close('all')
>>> data.plot()
>>> plt.show()
>>> f,p=signal.periodogram(data)
>>> plt.plot(f,p)
>>> plt.show()
>>> exit()
$ 
```
