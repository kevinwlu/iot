# <a href="https://goo.gl/6BsKOa">Lesson 7</a>: Cloud Platforms

## ThingSpeak

### Sign up and log in ThingSpeak at

https://thingspeak.com

### Create new channel cpu_loop with field1 cpu_pc and field2 mem_avail_mb

sudo pip3 install -U psutil

cd demo

cp ~/iot/lesson7/thingspeak_cpu_loop.py .

### Copy the Write API Key from

https://thingspeak.com/channels

nano thingspeak_cpu_loop.py

### Run thingspeak_cpu_loop.py

python3 thingspeak_cpu_loop.py

## Google Sheets

### Sign up and log in the Google Cloud Platform Identity and Access Management (IAM) at

https://console.developers.google.com/projectselector/iam-admin/iam

### Click "Create" and enter the project name, e.g., rpidata

### &equiv; > APIs & Services > + Enable APIs & Services > Enable Drive API and Sheets API

### Credential > Create Credentials > Create service account key > Service account > rpidata > JSON key type > Create > download rpidata-xxxxxxxxxxxx.json

### Install gspread and oauth2client

sudo pip3 install -U gspread oauth2client

cd demo

cp ~/iot/lesson3/system_info.py .

cp ~/iot/lesson7/rpi_spreadsheet.py .

### Ether move or secure copy the JSON key file to the same directory as rpi_spreadsheet.py

mv ~/Downloads/rpidata-*.json ~/demo

scp rpidata-*.json pi@155.246.200.x:/home/pi/demo

### Go to Google Sheets at

https://docs.google.com/spreadsheets/u/0

### Start a new spreadsheet rpidata

### Share the spreadsheet with the "client_email" address in the .json file, select “Can edit,” and click "Send"

#### Will receive an email with the subject "Delivery Status Notification (Failure)" and the message "Address not found" from mailer-daemon@google.com

### Delete Rows 2 to 1000, and enter Date / Time, CPU Usage %, Temperature C to header cells

### GDOCS_OAUTH_JSON = 'rpidata-*.json' and GDOCS_SPREADSHEET_NAME = 'rpidata'

nano rpi_spreadsheet.py

### Run rpi_spreadsheet.py

python3 rpi_spreadsheet.py
