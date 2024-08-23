# Lesson 7: Cloud Platforms

* [AAA (computer security)](https://en.wikipedia.org/wiki/AAA_(computer_security))
  * [Authentication](https://en.wikipedia.org/wiki/Authentication) (AuthN)
  * [Authorization](https://en.wikipedia.org/wiki/Authorization) (AuthZ)
  * Accounting ([Audit trail](https://en.wikipedia.org/wiki/Audit_trail))
  * [RADIUS](https://en.wikipedia.org/wiki/RADIUS) (Remote Authentication Dial-In User Service)
  * [TACACS](https://en.wikipedia.org/wiki/TACACS) (Terminal Access Controller Access-Control System)
* [Single sign-on](https://en.wikipedia.org/wiki/Single_sign-on) (SSO)
  * [Okta, Inc.](https://en.wikipedia.org/wiki/Okta,_Inc.)
  * [Okta](https://en.wikipedia.org/wiki/Okta) is a unit for measurement of the [cloud cover](https://en.wikipedia.org/wiki/Cloud_cover) ranging from 0 oktas (completely clear sky) through to 8 oktas (completely [overcast](https://en.wikipedia.org/wiki/Overcast))
  * [Octave](https://en.wikipedia.org/wiki/Octave) is a series of eight notes occupying the interval between (and including) two notes, one having twice the frequency of vibration of the other
* [Zero trust security model](https://en.wikipedia.org/wiki/Zero_trust_security_model)
* [ThingSpeak](https://en.wikipedia.org/wiki/ThingSpeak)
  * [MATLAB](https://en.wikipedia.org/wiki/MATLAB) (Matrix Laboratory)
  * [MATLAB Mobile](https://www.mathworks.com/products/matlab-mobile.html)
* [Pickle](https://docs.python.org/3/library/pickle.html): Python object serialization
* [gspread](https://gspread.readthedocs.io/en/latest)
* [OAuth](https://en.wikipedia.org/wiki/OAuth)
* [OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)
* [DHT](https://learn.adafruit.com/dht)11, DHT22, and AM2302 humidity-temperature sensor
  * Adafruit CircuitPython DHT [repository](https://github.com/adafruit/Adafruit_CircuitPython_DHT)
  * Adafruit Python DHT [repository](https://github.com/adafruit/Adafruit_Python_DHT) - Deprecated
* [BMP280](https://www.adafruit.com/product/2651) I2C or SPI barometric pressure-temperature-altitude sensor
  * Adafruit CircuitPython BMP280 [repository](https://github.com/adafruit/Adafruit_CircuitPython_BMP280)
* [BMP180](https://www.adafruit.com/product/1603) I2C barometric pressure-temperature-altitude sensor - Discontinued
  * Adafruit Python BMP [repository](https://github.com/adafruit/Adafruit_Python_BMP) - Deprecated
* [Eclipse Streamsheets](https://github.com/eclipse/streamsheets)
  * [No-code development platform](https://en.wikipedia.org/wiki/No-code_development_platform) (NCDP)

## Lab 7A: ThingSpeak

* Sign up and log in [ThingSpeak](https://thingspeak.com)
* Create new channel cpu_loop with field1 cpu_pc and field2 mem_avail_mb
* Copy the Write API Key from [channels](https://thingspeak.com/channels)
* [ThingSpeak licensing FAQ](https://thingspeak.com/pages/license_faq) (frequently asked questions)
### Review and run thingspeak_feed.py
```sh
$ sudo pip3 install -U psutil
$ cd ~/demo
$ cp ~/iot/lesson7/thingspeak_cpu_loop.py .
$ cp ~/iot/lesson7/thingspeak_feed.py .
$ cat thingspeak_cpu_loop.py
$ cat thingspeak_feed.py
$ python3 thingspeak_feed.py
An API key savefile was not found. Enter Write API Key >>>
Should we save this key for future use? [y/N] >>>
```
* If yes, the Write API Key is saved in API_KEY.pickle
* Alternatively, replace YOURKEYHERE with the Write API in Line 10 of thingspeak_cpu_loop.py
## Lab 7B: Google Sheets
* The following rpidata project and [rpi_spreadsheet.py](/lesson7/rpi_spreadsheet.py) require Raspberry Pi and system_info.py
* Alternatively, follow the same steps for a cpudata project and run [cpu_spreadsheet.py](/lesson7/cpu_spreadsheet.py) that does not require Raspberry Pi and system_info.py

### Sign up and log in the Google Cloud Platform Identity and Access Management [(IAM)](https://console.developers.google.com/projectselector/iam-admin/iam)

* Click "Create" and enter the project name, e.g., rpidata
* &equiv; > APIs & Services > + Enable APIs & Services > Enable both Drive API and Sheets API
* Credential > Create Credentials > Create service account key > Service account > rpidata > JSON key type > Create > download rpidata-xxxxxxxxxxxx.json

### Install gspread and oauth2client
```sh
$ sudo pip3 install -U gspread oauth2client
```
### Copy system_info.py and rpi_spreadsheet.py to ~/demo
* On older versions of Raspberry Pi OS before Bullseye, change /usr/bin/vcgencmd to /opt/vc/bin/vcgencmd in system_info.py
```sh
$ cd demo
$ cp ~/iot/lesson3/system_info.py .
$ cp ~/iot/lesson7/rpi_spreadsheet.py .
```
### If the JSON key file (* = xxxxxxxxxxxx) is on a different computer, secure copy it to the same directory as rpi_spreadsheet.py
```sh
$ scp rpidata-*.json pi@192.168.x.xxx:/home/pi/demo
```
### If the the JSON key file is on a Raspberry Pi, move it to the same directory as rpi_spreadsheet.py
```sh
$ mv ~/Downloads/rpidata-*.json ~/demo
```
### [How to copy files from Windows to Ubuntu in WSL on the same host](https://linuxhint.com/copy-files-from-windows-ubuntu-wsl-same-host/)

### Go to [Google Sheets](https://docs.google.com/spreadsheets/u/0)

* Start a new spreadsheet rpidata (or cpudata)
* Share the spreadsheet with the "client_email" address in the .json file, select “Can edit,” and click "Send"
  * May receive an email with the subject "Delivery Status Notification (Failure)" and the message "Address not found" from mailer-daemon@google.com
* Delete Rows 2 to 1000, and enter Date / Time, CPU Usage %, Temperature C (or Memory Available GB for cpudata) to header cells
  * This deletion is not necessary with the improved [rpi_worksheet.py](/lesson7/rpi_worksheet.py) and [cpu_worksheet.py](/lesson7/cpu_worksheet.py) that can check the next empty row to write data

### Edit rpi_spreadsheet.py

```sh
$ nano rpi_spreadsheet.py
```
> GDOCS_OAUTH_JSON = 'rpidata-xxxxxxxxxxxx.json'

> GDOCS_SPREADSHEET_NAME = 'rpidata'

### Run rpi_spreadsheet.py
```sh
$ python3 rpi_spreadsheet.py
```
