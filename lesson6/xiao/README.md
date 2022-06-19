# Seeed XIAO BLE Sense
* [Seeed Studio](https://github.com/Seeed-Studio)
* [Getting started with XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO_BLE/) on Windows
  * [Arduino IDE](https://www.arduino.cc/en/software)
  * [nRF52840](https://www.nordicsemi.com/Products/nRF52840)
  * [adafruit-nrfutil](https://github.com/adafruit/Adafruit_nRF52_nrfutil)
  * Arduino IDE > File > Preferences > Settings > Additional Boards Manager URLs > https://files.seeedstudio.com/arduino/package_seeeduino_boards_index.json > OK
  * Arduino IDE > Tools > Board > Board Manager > seeed nrf52 > Seeed nRF52 Boards > 2.6.1 > Install
  * Arduino IDE > Tools > Board > Seeed nRF Boards > Seeed XIAO BLE Sense - nRF52840
  * Arduino IDE > Tools > Port > COM* (Seeed XIAO BLE Sense - nRF52840)
* [Setup Arduino IDE on Raspberry Pi to support Seeed XIAO BLE Sense](https://www.youtube.com/watch?v=9OsbFAFQtnk)
* Seeed XIAO BLE Sense with Arduino IDE on Raspberry Pi OS > exec: "adafruit-nrfutil": executable file not found in $PATH > Error compiling for board Seeed XIAO nRF52840 Sense
```sh
pi@raspberrypy:~ $ pip3 install --user adafruit-nrfutil
pi@raspberrypy:~ $ adafruit-nrfutil version
adafruit-nrfutil version 0.5.3.post17
```
* Seeed XIAO BLE Sense with Arduino IDE on macOS > /Users/.../Library/Arduino15/packages/Seeeduino/hardware/nrf52/2.6.1/tools/adafruit-nrfutil/macos/adafruit-nrfutil: permission denied > Error compiling for board Seeed XIAO BLE Sense - nRF52840
```sh
$ cd Library/Arduino15/packages/Seeeduino/hardware/nrf52/2.6.1/tools/adafruit-nrfutil/macos/
$ chmod +x adafruit-nrfutil
$ ./adafruit-nrfutil version
adafruit-nrfutil version 0.5.3.post12
```
![blink.gif](/lesson6/blink.gif)
* [6-Axis IMU Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-IMU-Usage/)
  * 6-axis [inertial measurement unit](https://en.wikipedia.org/wiki/Inertial_measurement_unit) (IMU)
  * [Seeed_Arduino_LSM6DS3](https://github.com/Seeed-Studio/Seeed_Arduino_LSM6DS3) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library 
  * Arduino IDE > File > Examples > Seeed Arduino LSM6DS3 > [HighLevelExample](/lesson6/xiao/HighLevelExample.ino) > Upload
  * [LSM6DS3](https://content.arduino.cc/assets/st_imu_lsm6ds3_datasheet.pdf) iNEMO inertial module: always-on 3D accelerometer and 3D gyroscope
* [PDM microphone Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-PDM-Usage/)
  * [Pulse-density modulation](https://en.wikipedia.org/wiki/Pulse-density_modulation) (PDM) microphone
  * [Seeed_Arduino_Mic](https://github.com/Seeed-Studio/Seeed_Arduino_Mic) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library 
  * Arduino IDE > File > Examples > Seed Arduino Mic > [mic_serial_plotter](/lesson6/xiao/mic_serial_plotter.ino) > Upload
  * [Getting started with Wio terminal](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)
  * Interrupt service routines (ISR) also known as [interrupt handler](https://en.wikipedia.org/wiki/Interrupt_handler)
* [View Serial Monitor Over HC-05 Bluetooth Module](https://create.arduino.cc/projecthub/millerman4487/view-serial-monitor-over-bluetooth-fbb0e5)
  * Windows Settings > Devices > Bluetooth & other devices > Add Bluetooth or other devices > Bluetooth
* [Bluetooth Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-Bluetooth-Usage/)
  * [ArduinoBLE](https://github.com/arduino-libraries/ArduinoBLE) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library 
  * Arduino IDE > File > Examples > INCOMPATIBLE > ArduinoBLE > Peripheral > [LED](/lesson6/xiao/LED.ino) > Upload
  * Arduino IDE > Tools > Serial Monitor
  * [LightBlue](https://punchthrough.com/lightblue/) apps by Punch Through > Peripherals Nearby > Arduino
  * [Web Bluetooth API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API)
    * [MDN Web Docs](https://en.wikipedia.org/wiki/MDN_Web_Docs)
  * [Web Bluetooth demos](https://github.com/WebBluetoothCG/demos)
* [Motion Recognition Based on Edge Impulse](https://wiki.seeedstudio.com/XIAOEI/)
  * [U8g2 Monochrome Display Library](https://github.com/olikraus/u8g2)
  * [Edge Impulse](https://www.edgeimpulse.com/)
  * [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation)