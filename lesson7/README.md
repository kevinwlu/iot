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

### Sign up and log in Google Cloud Identity and Access Management (IAM) at

https://console.developers.google.com/projectselector/iam-admin/iam

### Click "Create" and enter the project name rpidata

### Click  Google APIs, select Google Drive API, then enable it

### Click Create Credentials, select service account, then create

### Select JSON key type and click Create key to download rpidata-*.json

### Install gspread and oauth2client

sudo pip3 install gspread oauth2client

cd demo

cp ~/iot/lesson3/system_info.py .

cp ~/iot/lesson7/rpi_spreadsheet.py .

mv ~/Downloads/rpidata-*.json ~/demo

### Go to Google Sheets at

https://docs.google.com/spreadsheets/u/0

### Start a new spreadsheet rpidata

### Share the spreadsheet with the "client_email" address in the .json file, select “Can edit,” and click "Send"

### Delete Rows 2 to 1000, and enter Date / Time, CPU Usage %, Temperature C to header cells

### GDOCS_OAUTH_JSON = 'rpidata-*.json' and GDOCS_SPREADSHEET_NAME = 'rpidata'

nano rpi_spreadsheet.py

### Run rpi_spreadsheet.py

python3 rpi_spreadsheet.py
