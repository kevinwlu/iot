# Lesson 7: Cloud Platforms

* [MATLAB](https://en.wikipedia.org/wiki/MATLAB) (Matrix Laboratory)
* [Pickle](https://docs.python.org/3/library/pickle.html): Python object serialization
* [ThingSpeak](https://en.wikipedia.org/wiki/ThingSpeak)
* [OAuth](https://en.wikipedia.org/wiki/OAuth)
* [OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)

## Lab 7A: ThingSpeak

### Sign up and log in [ThingSpeak](https://thingspeak.com)

### Create new channel cpu_loop with field1 cpu_pc and field2 mem_avail_mb

### Copy the Write API Key from [channels](https://thingspeak.com/channels)

### Review and run thingspeak_feed.py
```sh
$ sudo pip3 install -U psutil
$ cd ~/iot/lesson7
$ cat thingspeak_feed.py
$ python3 thingspeak_feed.py
```
## Lab 7B: Google Sheets

### Sign up and log in the Google Cloud Platform Identity and Access Management [(IAM)](https://console.developers.google.com/projectselector/iam-admin/iam)

* Click "Create" and enter the project name, e.g., rpidata
* &equiv; > APIs & Services > + Enable APIs & Services > Enable both Drive API and Sheets API
* Credential > Create Credentials > Create service account key > Service account > rpidata > JSON key type > Create > download rpidata-xxxxxxxxxxxx.json

### Install gspread and oauth2client
```sh
$ sudo pip3 install -U gspread oauth2client
$ cd demo
$ cp ~/iot/lesson3/system_info.py .
$ cp ~/iot/lesson7/rpi_spreadsheet.py .
```
### If the JSON key file (* = xxxxxxxxxxxx) is on a laptop computer, secure copy it to the same directory as rpi_spreadsheet.py
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
