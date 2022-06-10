# Seeed XIAO BLE Sense
* [GitHub](https://github.com/Seeed-Studio)
* [Getting started with XIAO BLE (Sense)](https://wiki.seeedstudio.com/XIAO_BLE/)
* [Setup Arduino IDE on Raspberry Pi to support Seeed XIAO BLE (Sense)](https://www.youtube.com/watch?v=9OsbFAFQtnk)
* [nRF52840](https://www.nordicsemi.com/Products/nRF52840)
* [adafruit-nrfutil](https://github.com/adafruit/Adafruit_nRF52_nrfutil)
* Seeed XIAO BLE (Sense) with Arduino IDE on Raspberry Pi OS > exec: "adafruit-nrfutil": executable file not found in $PATH > Error compiling for board Seeed XIAO nRF52840 Sense
```sh
pi@raspberrypy:~ $ pip3 install --user adafruit-nrfutil
pi@raspberrypy:~ $ adafruit-nrfutil version
adafruit-nrfutil version 0.5.3.post17
```
* Seeed XIAO BLE (Sense) with Arduino IDE on macOS > /Users/.../Library/Arduino15/packages/Seeeduino/hardware/nrf52/2.6.1/tools/adafruit-nrfutil/macos/adafruit-nrfutil: permission denied > Error compiling for board Seeed XIAO BLE Sense - nRF52840
```sh
$ cd Library/Arduino15/packages/Seeeduino/hardware/nrf52/2.6.1/tools/adafruit-nrfutil/macos/
$ chmod +x adafruit-nrfutil
$ ./adafruit-nrfutil version
adafruit-nrfutil version 0.5.3.post12
```
![blink.gif](/lesson6/blink.gif)
* [Bluetooth Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-Bluetooth-Usage/)
  * [LightBlue](https://punchthrough.com/lightblue/) apps by Punch Through
  * Arduino IDE > File > Examples > INCOMPATIBLE > ArduinoBLE > Peripheral > [LED](/lesson6/xiao/LED.ino)
* [6-Axis IMU Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-IMU-Usage/)
  * 6-axis [inertial measurement unit](https://en.wikipedia.org/wiki/Inertial_measurement_unit) (IMU)
  * Arduino IDE > File > Examples > Seeed Arduino LSM6DS3 > [HighLevelExample](/lesson6/xiao/HighLevelExample.ino)
  * [LSM6DS3](https://content.arduino.cc/assets/st_imu_lsm6ds3_datasheet.pdf) iNEMO inertial module: always-on 3D accelerometer and 3D gyroscope
* [PDM Microphone Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-PDM-Usage/)
  * [Pulse-density modulation](https://en.wikipedia.org/wiki/Pulse-density_modulation) (PDM) microphone
  * Arduino IDE > File > Examples > Seed Arduino Mic > [mic_serial_plotter](/lesson6/xiao/mic_serial_plotter.ino)
  * [Getting started with Wio terminal](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)
  * Interrupt service routines (ISR) also known as [interrupt handler](https://en.wikipedia.org/wiki/Interrupt_handler)
