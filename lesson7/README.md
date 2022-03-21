# Lesson 7: Cloud Platforms

* [AAA (computer security)](https://en.wikipedia.org/wiki/AAA_(computer_security))
  * [Authentication](https://en.wikipedia.org/wiki/Authentication) (AuthN)
  * [Authorization](https://en.wikipedia.org/wiki/Authorization) (AuthZ)
  * Accounting ([Audit trail](https://en.wikipedia.org/wiki/Audit_trail))
* [ThingSpeak](https://en.wikipedia.org/wiki/ThingSpeak)
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
* The following rpidata project and rpi_spreadsheet.py require Raspberry Pi and system_info.py
* Alternatively, follow the same steps for a cpudata project and run cpu_spreadsheet.py that does not require Raspberry Pi and system_info.py

### Sign up and log in the Google Cloud Platform Identity and Access Management [(IAM)](https://console.developers.google.com/projectselector/iam-admin/iam)

* Click "Create" and enter the project name, e.g., rpidata
* &equiv; > APIs & Services > + Enable APIs & Services > Enable both Drive API and Sheets API
* Credential > Create Credentials > Create service account key > Service account > rpidata > JSON key type > Create > download rpidata-xxxxxxxxxxxx.json

### Install gspread and oauth2client
```sh
$ sudo pip3 install -U gspread oauth2client
```
### Copy system_info.py and rpi_spreadsheet.py to ~/demo
* On Raspberry Pi OS (Bullseye), change /opt/vc/bin/vcgencmd to /usr/bin/vcgencmd in system_info.py
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

### Go to [Google Sheets](https://docs.google.com/spreadsheets/u/0)

* Start a new spreadsheet rpidata
* Share the spreadsheet with the "client_email" address in the .json file, select “Can edit,” and click "Send"
  * Will receive an email with the subject "Delivery Status Notification (Failure)" and the message "Address not found" from mailer-daemon@google.com
* Delete Rows 2 to 1000, and enter Date / Time, CPU Usage %, Temperature C to header cells

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
