# ArduinoBLE
* [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth)
  * [SoftwareSerial Library](https://docs.arduino.cc/learn/built-in-libraries/software-serial)
  * [View Serial Monitor Over Bluetooth](https://create.arduino.cc/projecthub/millerman4487/view-serial-monitor-over-bluetooth-fbb0e5) Using a [HC-05](https://howtomechatronics.com/tutorials/arduino/arduino-and-hc-05-bluetooth-module-tutorial/)
    * Windows Settings > Devices > Bluetooth & other devices > Add Bluetooth or other devices > Bluetooth
  * [Martyn Currey](http://www.martyncurrey.com/about/), "[Connecting 2 Arduinos by Bluetooth Using a HC-05 and a HC-06: Easy Method Using CMODE](http://www.martyncurrey.com/connecting-2-arduinos-by-bluetooth-using-a-hc-05-and-a-hc-06-easy-method-using-cmode/)"
    * [HC-05_AT_MODE_01.ino](/lesson6/xiao/ble/HC-05_AT_MODE_01.ino)
    * [HC-06_01.ino](/lesson6/xiao/ble/HC-06_01.ino)
  * Martyn Currey, "[Connecting 2 Arduinos by Bluetooth Using a HC-05 and a HC-06: Pair, Bind, and Link](http://www.martyncurrey.com/connecting-2-arduinos-by-bluetooth-using-a-hc-05-and-a-hc-06-pair-bind-and-link/)"
    * [HC-05_02_38400.ino](/lesson6/xiao/ble/HC-05_02_38400.ino) and [HC-05_03_9600.ino](/lesson6/xiao/ArduinoBLE/HC-05_03_9600.ino)
    * [HC-06_01_9600.ino](/lesson6/xiao/ble/HC-06_01_9600.ino)
  * Martyn Currey, "[Arduino to Arduino by Bluetooth](http://www.martyncurrey.com/arduino-to-arduino-by-bluetooth/)"
    * [Arduino2Arduino_Main_01.ino](/lesson6/xiao/ble/Arduino2Arduino_Main_01.ino)
    * [Arduino2Arduino_Secondary_01.ino](/lesson6/xiao/ble/Arduino2Arduino_Secondary_01.ino)
    * [Arduino2Arduino_example2_RemoteTemp_Main.ino](/lesson6/xiao/ble/Arduino2Arduino_example2_RemoteTemp_Main.ino)
    * [Arduino2Arduino_example2_RemoteTemp_Secondary.ino](/lesson6/xiao/ble/Arduino2Arduino_example2_RemoteTemp_Secondary.ino)
* [Bluetooth Low Energy](https://en.wikipedia.org/wiki/Bluetooth_Low_Energy) (BLE)
  * [Bluetooth Low Energy Characteristics, a Beginner's Tutorial](https://devzone.nordicsemi.com/guides/short-range-guides/b/bluetooth-low-energy/posts/ble-characteristics-a-beginners-tutorial)
* [ArduinoBLE](https://github.com/arduino-libraries/ArduinoBLE)
  * [ArduinoBLE library](https://www.arduino.cc/reference/en/libraries/arduinoble/)
  * [Connecting Nano 33 BLE devices over Bluetooth](https://docs.arduino.cc/tutorials/nano-33-ble-sense/ble-device-to-device)
* [Arduino APDS9960 library](https://github.com/arduino-libraries/Arduino_APDS9960)
  * [Adafruit APDS9960 breakout](https://learn.adafruit.com/adafruit-apds9960-breakout)
* [Getting Started With Arduino BLE](https://create.arduino.cc/projecthub/monica/getting-started-with-bluetooth-low-energy-ble-ab4c94)
  * [Generic Access Profile](https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gap) (GAP)
  * [Generic Attribute Profile](https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gatt) (GATT)
  * [Universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (UUID)
  * [BLE Profiles and Services](https://www.bluetooth.com/specifications/specs/)
  * [BLE Characteristics](https://www.bluetooth.com/specifications/assigned-numbers/)
* [How to Use LightBlue: The Go-To BLE Development Tool](https://punchthrough.com/lightblue-features/)
  * The UUID shall be [16 bits](https://btprodspecificationrefs.blob.core.windows.net/assigned-values/16-bit%20UUID%20Numbers%20Document.pdf) or 128 bits
* [LightBlue Cloud Connect](https://punchthrough.com/introducing-cloud-connect-for-lightblue-explorer/)
  * This feature allows you to listen for BLE notifications or indications and send this stream of data to the cloud platform of your choice.
  * Supported platforms are [AWS](https://punchthrough.com/setting-up-aws-iot-with-lightblue-cloud-connect/) and [Adafruit IO](https://punchthrough.com/setting-up-adafruit-io-with-lightblue-cloud-connect/).
  * You'll be prompted for your platform API credentials if your enable the feature.
* [Get Started With Arduino Nano 33 BLE](https://www.okdo.com/getting-started/get-started-with-arduino-nano-33-ble/)
  * [hello.ino](/lesson6/xiao/ble/hello.ino)
  * [echo.ino](/lesson6/xiao/ble/echo.ino) includes read, write, and notify BLE characteristics, e.g., ```charac.writeValue(var);```
  * When the board is powered by a battery, comment out ```while(!Serial);``` that pauses the code until the Arduino IDE serial monitor is open
