# Seeed Studio XIAO Series
* [Seeed Studio](https://github.com/Seeed-Studio)
* [XIAO Series](https://www.seeedstudio.com/xiao-series-page)
* [Getting Started with Seeed Studio XIAO ESP32S3 (Sense)](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/)
  * [Wi-Fi usage with Seeed Studio XIAO ESP32S3 (Sense)](https://wiki.seeedstudio.com/xiao_esp32s3_wifi_usage/)
  * [Pin multiplexing with Seeed Studio XIAO ESP32S3 (Sense)](https://wiki.seeedstudio.com/xiao_esp32s3_pin_multiplexing/)
* [Getting started with Seeed Studio XIAO nRF52840 (Sense)](https://wiki.seeedstudio.com/XIAO_BLE/) on Windows
  * [Arduino IDE](https://www.arduino.cc/en/software)
  * [nRF52840](https://www.nordicsemi.com/Products/nRF52840) by [Nordic Semiconductor](https://en.wikipedia.org/wiki/Nordic_Semiconductor)
  * [Floating-point unit](https://en.wikipedia.org/wiki/Floating-point_unit) (FCU)
  * [Device Firmware Upgrade](https://en.wikipedia.org/wiki/USB#Device_Firmware_Upgrade_mechanism) (DFU)
  * [adafruit-nrfutil](https://github.com/adafruit/Adafruit_nRF52_nrfutil)
  * Arduino IDE > File > Preferences > Settings > Additional Boards Manager URLs > https://files.seeedstudio.com/arduino/package_seeeduino_boards_index.json > OK
  * Arduino IDE > Tools > Board > Board Manager > seeed nrf52 > Seeed nRF52 Boards > 2.7.2 > Install
  * Arduino IDE > Tools > Board > Seeed nRF Boards > Seeed XIAO BLE Sense - nRF52840
  * Quit Arduino IDE
  * Arduino IDE > Tools > Port > COM* (Seeed XIAO BLE Sense - nRF52840)
* Collaborators
  * [Sean Pelcher](https://github.com/seanpelcher)
  * [Francesca Tannenbaum](https://github.com/ftannenbaum)
  * [Omar El Sayed](https://github.com/oelsayed10)
* [Setup Arduino IDE on Raspberry Pi to support Seeed XIAO BLE Sense](https://www.youtube.com/watch?v=9OsbFAFQtnk)
* Seeed XIAO BLE Sense with Arduino IDE on Raspberry Pi OS > exec: "adafruit-nrfutil": executable file not found in $PATH > Error compiling for board Seeed XIAO nRF52840 Sense
```sh
pi@raspberrypy:~ $ pip3 install --user adafruit-nrfutil
pi@raspberrypy:~ $ adafruit-nrfutil version
adafruit-nrfutil version 0.5.3.post17
```
* Seeed XIAO BLE Sense with Arduino IDE on macOS > /Users/.../Library/Arduino15/packages/Seeeduino/hardware/nrf52/2.6.1/tools/adafruit-nrfutil/macos/adafruit-nrfutil: permission denied > Error compiling for board Seeed XIAO BLE Sense - nRF52840
  * The subfolder name nrf52 for versions 2.6.1 and 1.0.0 becomes mbed for version 2.7.2 with executable adafruit-nrfutil
```sh
$ cd Library/Arduino15/packages/Seeeduino/hardware/nrf52/2.6.1/tools/adafruit-nrfutil/macos/
$ chmod +x adafruit-nrfutil
$ ./adafruit-nrfutil version
adafruit-nrfutil version 0.5.3.post12
```
![blink.gif](/lesson6/xiao/blink.gif)
![battery.gif](/lesson6/xiao/battery.gif)
* A [deep sleep example](https://github.com/0hotpotman0/BLE_52840_Core/blob/main/libraries/Bluefruit52Lib/examples/Hardware/deep_Sleep/deep_Sleep.ino) showed [power consumption](https://wiki.seeedstudio.com/XIAO_BLE/#power-consumption-verification) about 3&micro;A
  * A fully charged 3.7 V 100 mAh [lithium polymer battery](https://en.wikipedia.org/wiki/Lithium_polymer_battery) may power the blink example up to 68 hours and 52 hours for the first and second times, respectively
  * Arduino IDE > File > Examples > Build-in Examples > 01.Basics > Blink
  * Keeping the battery above 50% is recommended
* [6-Axis IMU Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-IMU-Usage/)
  * [Inertial measurement unit](https://en.wikipedia.org/wiki/Inertial_measurement_unit) (IMU)
  * [Seeed_Arduino_LSM6DS3](https://github.com/Seeed-Studio/Seeed_Arduino_LSM6DS3) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library 
  * Arduino IDE > File > Examples > Seeed Arduino LSM6DS3 > [HighLevelExample](/lesson6/xiao/HighLevelExample.ino) > Upload
  * [LSM6DS3](https://content.arduino.cc/assets/st_imu_lsm6ds3_datasheet.pdf) iNEMO inertial module: always-on 3D accelerometer and 3D gyroscope
* [PDM Microphone Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-PDM-Usage/)
  * [Pulse-code modulation](https://en.wikipedia.org/wiki/Pulse-code_modulation) (PCM)
  * [Pulse-density modulation](https://en.wikipedia.org/wiki/Pulse-density_modulation) (PDM)
  * [Adafruit PDM microphone breakout](https://learn.adafruit.com/adafruit-pdm-microphone-breakout/)
  * [MSM261D3526H1CPM](https://files.seeedstudio.com/wiki/XIAO-BLE/mic-MSM261D3526H1CPM-ENG.pdf) MEMS microphone
    * [Microelectromechanical systems](https://en.wikipedia.org/wiki/MEMS) (MEMS)
      * [Harvey C. Nathanson](https://en.wikipedia.org/wiki/Harvey_C._Nathanson) 1936&mdash;2019
    * [Nanoelectromechanical systems](https://en.wikipedia.org/wiki/Nanoelectromechanical_systems) (NEMS)
      * [Molecular machine](https://en.wikipedia.org/wiki/Molecular_machine)
      * [Fraser Stoddart](https://en.wikipedia.org/wiki/Fraser_Stoddart) 1942&mdash;2024
  * [Seeed_Arduino_Mic](https://github.com/Seeed-Studio/Seeed_Arduino_Mic) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library 
  * Arduino IDE > File > Examples > Seed Arduino Mic > [mic_serial_plotter](/lesson6/xiao/mic_serial_plotter.ino) > Upload
  * [Getting started with Wio terminal](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)
  * [Thin-film-transistor liquid-crystal display](https://en.wikipedia.org/wiki/Thin-film-transistor_liquid-crystal_display) (TFT LCD)
  * [Direct memory access](https://en.wikipedia.org/wiki/Direct_memory_access) (DMA)
  * Interrupt service routines (ISR) also known as [interrupt handler](https://en.wikipedia.org/wiki/Interrupt_handler)
  * [Wio audio spectrum display](https://macsbug.wordpress.com/2020/05/28/wio-audio-spectrum-display/)
* [Speech Recognition on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-TFLite-Mic/)
  * [Arduino_TensorFlowLite](https://github.com/lakshanthad/tflite-micro-arduino-examples) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library
  * Arduino IDE > File > Examples > Arduino_TensorFlowLite > [micro_speech](/lesson6/xiao/micro_speech.ino) > Upload
* [Bluetooth Usage on XIAO BLE Sense](https://wiki.seeedstudio.com/XIAO-BLE-Sense-Bluetooth-Usage/)
  * [ArduinoBLE](https://github.com/arduino-libraries/ArduinoBLE) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library 
  * Arduino IDE > File > Examples > INCOMPATIBLE > ArduinoBLE > Peripheral > [LED](/lesson6/xiao/ble/Peripheral/LED.ino) > Upload
  * Arduino IDE > Tools > Serial Monitor
  * When the board is powered by a battery, comment out ```while(!Serial);``` that pauses the code until the Arduino IDE serial monitor is open
  * [LightBlue](https://punchthrough.com/lightblue/) apps by Punch Through > Peripherals Nearby > Arduino
    * [How to Use LightBlue: The Go-To BLE Development Tool](https://punchthrough.com/lightblue-features/)
    * [Punch Through GitHub repository](https://github.com/punchthrough)
  * [Web Bluetooth API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API)
    * [MDN Web Docs](https://en.wikipedia.org/wiki/MDN_Web_Docs)
  * [Web Bluetooth demos](https://github.com/WebBluetoothCG/demos)
* [Motion Recognition Based on Edge Impulse](https://wiki.seeedstudio.com/XIAOEI/)
  * [U8g2 Monochrome Display Library](https://github.com/olikraus/u8g2) > Code > Download ZIP
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library
  * Arduino IDE > [XIAO-display.ino](/lesson6/xiao/XIAO-display.ino)
  * Arduino IDE > [XIAO-gestures.ino](/lesson6/xiao/XIAO-gestures.ino)
  * [Edge Impulse](https://www.edgeimpulse.com/)
    * [Getting started](https://docs.edgeimpulse.com/docs/)
    * [Projects](https://docs.edgeimpulse.com/experts/)
    * [Spectral features](https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks/spectral-features)
  * Edge Impulse > Create new project > XIAO-BLE-gestures > Developer (20 min job limit, 4GB or 4 hours of data, limited collaboration) > Accelerometer data > Let's get started
  * Open a terminal to install the [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-installation) that requires [Python 3](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/en/download/), e.g., node 16.15.1 and npm 8.11.0
  * Run the [Edge Impulse Data Forwarder](https://docs.edgeimpulse.com/docs/edge-impulse-cli/cli-data-forwarder) to connect the XIAO BLE Sense
    * [Frequency](https://en.wikipedia.org/wiki/Frequency)
    * [Baud](https://en.wikipedia.org/wiki/Baud)
  * Edge Impulse > Data acquisition > Record new data > Label: left-right > Sample length (ms.): 20000 > Frequency: 50Hz > Start sampling > Collected data > &vellip; > Split Sample > + Add Segment per second > Split
  * Data acquisition > Record new data > Label: idle > &hellip;
  * Data acquisition > Record new data > Label: up-down > &hellip;
  * Dashboard > Danger zone > Perform train / test split > Yes, perform the train / test split > Confirm > Dataset was rebalanced > OK
  * Impulse design > Create impulse > Time series data > Uncheck "Zero-pad data" > Add a processing block > Spectral Analysis > Add a learning block > Classification (Keras) > Save Impulse
  * Impulse design > Spectral features > Save parameters > Check "Calculate feature importance" > Generate features
  * Impulse design > NN Classifier > Check "Auto-balance dataset" > Start training
  * Model testing > Classify all
  * Deployment > Arduino library > Build > XIAO-BLE-gestures_inferencing.zip
  * Arduino IDE > Sketch > Include Library > Add .ZIP Library
  * Arduino IDE > File > Examples > XIAO-BLE-gestures_inferencing
  * Arduino IDE > [XIAOEI.ino](/lesson6/xiao/XIAOEI.ino)

On Windows
```sh
npm install -g edge-impulse-cli --force
edge-impulse-data-forwarder
```
> If "edge-impulse-data-forwarder.ps1 cannot be loaded because running scripts is disabled on this system," update Windows PowerShell execution policy with the following command to allow running scripts 
```sh
Set-ExecutionPolicy unrestricted
```
On macOS
```sh
sudo npm install -g edge-impulse-cli --force
edge-impulse-data-forwarder
```
> If edge-impulse-data-forwarder command not found
```sh
sudo chown -R $USER /usr/local/lib/node_modules
```
On both Windows and macOS
> Sensor reading shall be all numbers
```sh
What is your user name or e-mail address(edgeimpulse.com)?
What is your password?
To which project do you want to connect this device? Motion Recognition with XIAO BLE SENSE
3 sensor axes detected (example values: [9.6105,-15.7887,-2.7459]). What do you want to call them? Separate the names 
with ',': Ax,Ay,Az
What name do you want to give this device? XIAO BLE SENSE
```
To clean the configuration
```sh
edge-impulse-data-forwarder --clean
```
To override the frequency
```sh
edge-impulse-data-forwarder --frequency 100
```
To set a different baud rate
```sh
edge-impulse-data-forwarder --baud-rate 460800
```
